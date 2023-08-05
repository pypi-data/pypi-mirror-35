#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os

import dotenv
from invoke import run
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater, CallbackQueryHandler

from .utils import stats_summary

dotenv.load_dotenv(dotenv.find_dotenv())

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('dstack_cubed')

token = os.getenv('TELEGRAM_BOT_TOKEN')
admin1 = Filters.user(username=os.getenv('TELEGRAM_BOT_ADMIN1'))
admin2 = Filters.user(username=os.getenv('TELEGRAM_BOT_ADMIN2'))


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text("""
    Available commands:
    /start - shows this help
    /stats - shows server stats
    /restart - asks which service to restart
    """)


def invoke(bot, update):
    """Run message as invoke task"""
    result = run(update.message.text, hide=True, warn=True, pty=False)
    update.message.reply_markdown(f'```bash\n{result.stdout or "No output."}\n```')


def error(bot, update, error_name):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error_name)


def stats(bot, update):
    update.message.reply_markdown(f'```bash\n{stats_summary()}\n```')


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
        text=f'{result.stdout or "No output."}',
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
    dp.add_handler(CommandHandler("stats", stats, filters=admin1 | admin2))
    dp.add_handler(CommandHandler("restart", restart, filters=admin1 | admin2))
    # on non-command i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & (admin1 | admin2), invoke))
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
