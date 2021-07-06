#built in
import os
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
        nums = input('Select the bots you wish to select by listing the number corrosponding (e.g. 1 2 4): ')
        nums = nums.split(' ')
        try:
            nums = sorted(list(map(int, nums)))
            break
        except ValueError as e:
            print(e)
    return nums

def eula():
    agreement = 'To use this program, you must agree to the EULA included.\nIf you agree to the CC1.0 LICENSE included by Chisaku-Dev switch the FALSE to a TRUE below\nFALSE'
    if 'eula.txt' not in os.listdir(os.path.dirname(os.path.abspath(__file__))):
        eula = open('eula.txt', 'w')
        eula.write(agreement)
        eula.close()
        print('eula.txt has been generated, please agree to the EULA included')
        quit()
    else:
        eula = open('eula.txt', 'r')
        agree = eula.readlines()
        if agree[2].upper() == 'TRUE':
            return True
        else:
            print('You must agree to the EULA included.')
            quit()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    eula()
    subprocess.call(f'pip3 install discord', shell=False)
    print('discord library has been installed')
    while True:
        try:
            choices = ['Add bot(s)', 'Remove bot(s)', 'Boot all', 'Boot specific', 'Boot w/o saving token', 'Stop Specific', 'Restart Specific', 'Quit']
            while True:
                ui.num_list(choices)
                try:
                    choice = int(input('Enter the number you wish to execute:\n'))
                    break
                except ValueError as e:
                    ui.sys_message(e)
            if choices[choice] == 'Add bot(s)':
                tks = input('What is your bot token(s) (if multiple, seperate them with spaces)? Obtain it from https://discord.com/developers/ and paste it here: ')
                tks = tks.split(' ')
                for tk in tks:
                    data.save(tk, input('Prefix: '))
                ui.sys_message('Success')
            elif choices[choice] == 'Remove bot(s)':
                bot = data.extract()
                ui.num_list(bot)
                if bot != []:
                    bot_rm_nums = inputs()
                    for bot_rm_num in offset(bot_rm_nums):
                        data.remove(bot_rm_num)
                    ui.sys_message('Success')
                else:
                    ui.sys_message('There are no bots stored')
            elif choices[choice] == 'Boot all':
                bots = data.extract()
                if bots != []:
                    for bot in bots:
                        core.boot(bot)
                else:
                    ui.sys_message('There are no bots stored')
            elif choices[choice] == 'Boot specific':
                bots = data.extract()
                ui.num_list(bots)
                if bots != []:
                    bot_stp_nums = inputs()
                    for bot_st_num in bot_stp_nums:
                        core.boot(bots[bot_st_num])
                else:
                    ui.sys_message('There are no bots stored')
            elif choices[choice] == 'Boot w/o saving token':
                tk = input('What is the bot token?\n')
                px = input('What is the desired bot prefix?\n')
                bot = dict(token = tk, prefix = px)
                core.boot(bot)
            elif choices[choice] == 'Restart Specific':
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
            elif choices[choice] == 'Stop Specific':
                core.list_threads()
                if core.processes != []:
                    bot_stp_nums = inputs()
                    for bot_stp_num in offset(bot_stp_nums):
                        core.stop(bot_stp_num)
                    ui.sys_message('Successfully stopped the bots')
                else:
                    ui.sys_message('There are no bots running')
            elif choices[choice] == 'Quit':
                quit()
        except Exception as e:
            print(f'There has been an error: {e}')
