#built in
from multiprocessing import Process
#self
import basicbot

processes = []

def boot(token):
    processes.append((token, Process(target=basicbot.main, args=(token))))
    processes[-1][1].start()

def list_threads():
    print(processes)

def stop(bot_num):
    processes[bot_num][1].terminate()
    processes.remove(processes[bot_num])