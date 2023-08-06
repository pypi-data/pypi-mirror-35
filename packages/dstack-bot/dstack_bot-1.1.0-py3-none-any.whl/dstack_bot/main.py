#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import re

import dotenv
from invoke import run
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, TelegramError
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater, CallbackQueryHandler

from .exceptions import NotConfigured
from .utils import stats_summary, get_env

dotenv.load_dotenv(dotenv.find_dotenv())

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('dstack_cubed')

envs = [
    'TELEGRAM_BOT_TOKEN',
    'TELEGRAM_BOT_ADMIN1',
    'TELEGRAM_BOT_ADMIN2',
    'S3_BUCKET_NAME',
    'S3_BACKUP_PATH',
    'S3_BACKUP_TAG',
    'POSTGRES_CONTAINER_NAME',
    'POSTGRES_USERNAME',
]

try:
    token = get_env('TELEGRAM_BOT_TOKEN')
    admin1 = Filters.user(username=get_env('TELEGRAM_BOT_ADMIN1'))
    admin2 = Filters.user(username=get_env('TELEGRAM_BOT_ADMIN2'))
except NotConfigured as e:
    raise TelegramError(str(e))


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text("""
    Available commands:
    /start - shows this help
    /status - checks the status of the toolset service
    /stats - shows server stats
    /restart - asks which service to restart
    /users - download csv of the current users
    /backup - create backup and upload to s3 bucket
    /show_backups - Show list of most recent backups
    /shell - run arbitrary commands using dstack/invoke on the server.
    """)


def invoke(bot, update):
    """Run message as invoke task"""
    result = run(update.message.text[7:], hide=True, warn=True, pty=False)
    update.message.reply_markdown(f'```bash\n{result.stdout or result.stderr or "No output."}\n```')


def status(bot, update):
    """Run message as invoke task"""
    result = run("docker ps --format 'table {{.Names}}\t{{.Status}}'", hide=True, warn=True, pty=False)
    update.message.reply_markdown(f'```bash\n{result.stdout or result.stderr or "No output."}\n```')


def error(bot, update, error_name):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error_name)
    update.message.reply_markdown(f'```bash\n{error_name}\n```')


def stats(bot, update):
    update.message.reply_markdown(f'```bash\n{stats_summary()}\n```')


def users(bot, update):
    try:
        container_name = get_env('POSTGRES_CONTAINER_NAME')
        postgres_username = get_env('POSTGRES_USERNAME')
    except NotConfigured as e:
        raise TelegramError(str(e))
    path = '/tmp/users.csv'
    fields = ['username', 'email', 'first_name', 'last_name']
    update.message.reply_text('Download file below:')
    run(f'docker exec {container_name} psql -U {postgres_username} -c "'
        f"COPY (select {','.join(fields)} from auth_user) to '{path}' (format csv, delimiter ',');"
        '"', hide=True, warn=True, pty=False)
    run(f'docker cp {container_name}:{path} {path}', hide=True, warn=True, pty=False)
    bot.send_document(chat_id=update.message.chat_id, document=open('/tmp/users.csv', 'rb'))


def backup(bot, update):
    """Run message as invoke task"""
    tag = 'gauseng' or update.message.text[7:]
    result = run(f'dstack e db backup --tag {tag}', hide=True, warn=True, pty=False)
    update.message.reply_markdown(f'```bash\n{result.stdout or result.stderr or "No output."}\n```')


def show_backups(bot, update):
    try:
        bucket = get_env('S3_BUCKET_NAME')
        backup_path = get_env('S3_BACKUP_PATH')
        backup_tag = get_env('S3_BACKUP_TAG', '')
    except NotConfigured as e:
        raise TelegramError(str(e))

    tag = update.message.text[14:] or backup_tag
    backups = []
    result = run(f'aws s3 ls s3://{bucket}{backup_path}', hide=True, warn=True, pty=False)
    aws_ls = result.stdout.split('\n')
    for entry in aws_ls[:-1]:
        match = re.match('.+db_backup\.(?P<date>[\dT-]{19}Z)_(?P<tag>.+)\.tar\.gz$', entry)
        if match:
            data = match.groupdict()
            if tag:
                # filter on tag
                if tag == data['tag']:
                    backups.append(f"{data['date']} - {data['tag']}")
            else:
                # List all backups
                backups.append(f"{data['date']} - {data['tag']}")

    backups_print = '\n'.join(backups)
    update.message.reply_markdown(f"```bash\n{backups_print}\n```")


def restart(bot, update):
    # TODO: Populate the options dynamically from docker ps output
    keyboard = [
        [
            InlineKeyboardButton("Django", callback_data='django'),
            InlineKeyboardButton("Superset", callback_data='superset'),
        ],
        [
            InlineKeyboardButton("Nginx", callback_data='nginx'),
            InlineKeyboardButton("Redis", callback_data='redis'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_markdown('Select service to restart:', reply_markup=reply_markup)


def restart_service(bot, update):
    query = update.callback_query

    service = query.data
    result = run(f'docker restart toolset_{service}_1', hide=True, warn=True, pty=False)

    # TODO: Explicitly say if restart succeeded or failed.
    bot.edit_message_text(
        text=f'{result.stdout or result.stderr or "No output."}',
        chat_id=query.message.chat_id,
        message_id=query.message.message_id)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start, filters=admin1 | admin2))
    dp.add_handler(CommandHandler("help", start, filters=admin1 | admin2))
    dp.add_handler(CommandHandler("shell", invoke, filters=admin1 | admin2))
    dp.add_handler(CommandHandler("status", status, filters=admin1 | admin2))
    dp.add_handler(CommandHandler("stats", stats, filters=admin1 | admin2))
    dp.add_handler(CommandHandler("restart", restart, filters=admin1 | admin2))
    dp.add_handler(CommandHandler("backup", backup, filters=admin1 | admin2))
    dp.add_handler(CommandHandler("users", users, filters=admin1 | admin2))
    dp.add_handler(CommandHandler("show_backups", show_backups, filters=admin1 | admin2))
    # on non-command i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text & (admin1 | admin2), invoke))
    # TODO: Make sure this is secure
    dp.add_handler(CallbackQueryHandler(restart_service))
    # log all errors
    dp.add_error_handler(error)
    # Start the Bot
    updater.start_polling()
    logger.info('Bot started')
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
