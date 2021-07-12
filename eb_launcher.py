#built in
import os
import sys
import subprocess
#self
import ui
import data
import core

def offset(list):
    for i in range(0, len(list)):
        if i > 0:
            list[i] -= i
    return list

def inputs():
    while True:
        nums = input('Select the bots you wish to select by listing the number corrosponding (e.g. 1 2 4): ').split(' ')
        try:
            nums = sorted(list(map(int, nums)))
            break
        except ValueError as e:
            print(e)
    return nums

def eula():
    if 'LICENSE' not in os.listdir(os.path.dirname(os.path.abspath(__file__))):
        input('LICENSE does not exist; Please download it from https://github.com/chisaku-dev/EasyBot.py and try again')
        quit()
    else:
        input(f"{open('LICENSE', 'r').read()}\n [If you press ENTER, you agree to the LICENSE included]")

class commands:
    def help():
        ui.sys_message('Commands List')
        ui.list_dict(choices)
    def add():
        tks = input('What is your bot token(s) (if multiple, seperate them with spaces)? Obtain it from https://discord.com/developers/ and paste it here: ').split(' ')
        exist_tks = data.extract_tks()
        for tk in tks:
            if not tk in exist_tks:
                data.save(tk, input(f'Prefix for {tk}: '))
            else:
                print(tk, 'already exists in the database; Please remove the previous entry before trying to add this token again')
        ui.sys_message('Success')
    def rm():
        bot = data.extract()
        ui.num_list(bot)
        if bot != []:
            bot_rm_nums = inputs()
            for bot_rm_num in offset(bot_rm_nums):
                data.remove(bot_rm_num)
            ui.sys_message('Success')
        else:
            ui.sys_message('There are no bots stored')
    def boota():
        bots = data.extract()
        if bots != []:
            for bot in bots:
                core.boot(bot)
        else:
            ui.sys_message('There are no bots stored')
    def boots():
        bots = data.extract()
        ui.num_list(bots)
        if bots != []:
            bot_stp_nums = inputs()
            for bot_st_num in bot_stp_nums:
                core.boot(bots[bot_st_num])
        else:
            ui.sys_message('There are no bots stored')
    def boott():
        tk = input('What is the bot token?\n')
        px = input('What is the desired bot prefix?\n')
        bot = dict(token = tk, prefix = px)
        core.boot(bot)
    def restart():
        core.list_threads()
        if core.processes != []:
            bot_stp_nums = inputs()
            for bot_stp_num in offset(bot_stp_nums):
                bot = core.processes[bot_stp_num]
                core.stop(bot_stp_num)
                core.boot(dict(token = bot[0], prefix = bot[1]))
            ui.sys_message('Successfully restarted the bots')
        else:
            ui.sys_message('There are no bots running')
    def kill():
        core.list_threads()
        if core.processes != []:
            bot_stp_nums = inputs()
            for bot_stp_num in offset(bot_stp_nums):
                core.stop(bot_stp_num)
            ui.sys_message('Successfully stopped the bots')
        else:
            ui.sys_message('There are no bots running')
    def quit():
        if core.processes != []:
            for bots in range(0, len(core.processes)):
                core.stop(0)
        quit()
if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if not 'agreetos' in sys.argv:
        eula()
    try:
        os.mkdir('./data')
        open('./data/bots.easybot', 'w').close()
    except: pass
    try:
        os.mkdir('./cogs')
    except: pass
    subprocess.call(f'pip3 install discord', shell=False)
    print('discord library has been installed')
    choices = {
    'add': 'Add bot(s)',
    'rm': 'Remove bot(s)',
    'bootall':'Boot all',
    'bootspecific': 'Boot specific',
    'bootnotoken': 'Boot w/o saving token',
    'kill': 'Stop Specific',
    'restart': 'Restart Specific',
    'quit': 'Quit'
    }
    i = 1
    ui.sys_message('EasyBot.py is running')
    commands.help()
    while True:
        try:
            if i < len(sys.argv):
                choice = sys.argv[i]
                i += 1
            else:
                choice = input()
            if choice == 'help':
                commands.help()
            if choice == 'add':
                commands.add()
            elif choice == 'rm':
                commands.rm()
            elif choice == 'bootall':
                commands.boota()
            elif choice == 'bootspecific':
                commands.boots()
            elif choice == 'bootnotoken':
                commands.boott()
            elif choice == 'restart':
                commands.restart()
            elif choice == 'kill':
                commands.kill()
            elif choice == 'quit':
                commands.quit()
        except Exception as e:
            print(f'There has been an error: {e}')
