#built in
from multiprocessing import Process
#self
import basicbot

processes = []

def boot(prefix, token):
    processes.append((token, prefix, Process(target=basicbot.main, args=(token, prefix))))
    processes[-1][2].start()

def list_threads():
    print(processes)

def stop(bot_num):
    processes[bot_num][2].terminate()
    processes.remove(processes[bot_num])