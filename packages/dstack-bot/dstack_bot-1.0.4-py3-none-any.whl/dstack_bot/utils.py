import operator
from datetime import datetime

import psutil


def stats_summary():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    now = datetime.now()
    time_diff = "Online for: %.1f Hours" % (((now - boot_time).total_seconds()) / 3600)
    memory_total = "Total memory: %.2f GB " % (memory.total / 1000000000)
    memory_available = "Available memory: %.2f GB" % (memory.available / 1000000000)
    memory_used_percentage = "Used memory: " + str(memory.percent) + " %"
    disk_used = "Disk used: " + str(disk.percent) + " %"
    pids = psutil.pids()
    pids_reply = ''
    processes = {}
    for pid in pids:
        p = psutil.Process(pid)
        try:
            process_memory_percentage = p.memory_percent()
            if process_memory_percentage > 0.5:
                if p.name() in processes:
                    processes[p.name()] += process_memory_percentage
                else:
                    processes[p.name()] = process_memory_percentage
        except (psutil.AccessDenied, psutil.ZombieProcess):
            pass
    sorted_processes = sorted(processes.items(), key=operator.itemgetter(1), reverse=True)
    for process in sorted_processes:
        pids_reply += process[0] + " " + ("%.2f" % process[1]) + " %\n"

    return '\n'.join([time_diff, memory_total, memory_available, memory_used_percentage, disk_used, pids_reply])
