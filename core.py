#built in
import multiprocessing
#self
import basicbot, ui

processes = []

def boot(bot):
    processes.append((bot['token'], bot['prefix'], multiprocessing.Process(target=basicbot.main, args=(bot['token'], bot['prefix']))))
    processes[-1][2].start()

def list_threads():
    ui.num_list(processes)

def stop(bot_num):
    processes[bot_num][2].terminate()
    processes.remove(processes[bot_num])