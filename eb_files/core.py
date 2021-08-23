#built in
from multiprocessing import Process
#self
import basicbot, ui

processes = []

def boot(prefix, token):
    processes.append((token, prefix, Process(target=basicbot.main, args=(token, prefix))))
    processes[-1][2].start()

def list_threads():
    ui.num_list(processes)

def stop(bot_num):
    processes[bot_num][2].terminate()
    processes.remove(processes[bot_num])