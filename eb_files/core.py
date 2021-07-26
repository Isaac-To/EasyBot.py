#built in
from multiprocessing import Process
#self
from eb_files import basicbot, ui

processes = []

def boot(bot):
    processes.append((bot['token'], bot['prefix'], Process(target=basicbot.main, args=(bot['token'], bot['prefix']))))
    processes[-1][2].start()

def list_threads():
    ui.num_list(processes)

def stop(bot_num):
    processes[bot_num][2].terminate()
    processes.remove(processes[bot_num])