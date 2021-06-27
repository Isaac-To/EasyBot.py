#built in
import os
#self
import ui
import data
import core

if __name__ == '__main__':
    os.system('pip install discord /dev/null 2>&1')
    print('DiscordPy library has been installed')
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
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
                    while True:
                        bot_rm_nums = input('Select the bots you wish to remove by listing the number corrosponding (e.g. 1 2 4): ')
                        bot_rm_nums = bot_rm_nums.split(' ')
                        try:
                            bot_rm_nums = sorted(list(map(int, bot_rm_nums)))
                            break
                        except ValueError as e:
                            print(e)
                    for i in range(0, len(bot_rm_nums)):
                        if i > 0:
                            bot_rm_nums[i] -= i
                    for bot_rm_num in bot_rm_nums:
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
                    while True:
                        bot_st_nums = input('Select the bots you wish to boot by listing the number corrosponding (e.g. 1 2 4): ')
                        bot_st_nums = bot_st_nums.split(' ')
                        try:
                            bot_st_nums = sorted(list(map(int, bot_st_nums)))
                            break
                        except ValueError as e:
                            print(e)
                    for bot_st_num in bot_st_nums:
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
                    while True:
                        bot_stp_nums = input('Select the bots you wish to restart by listing the number corrosponding (e.g. 1 2 4): ')
                        bot_stp_nums = bot_stp_nums.split(' ')
                        try:
                            bot_stp_nums = sorted(list(map(int, bot_stp_nums)))
                            break
                        except ValueError as e:
                            print(e)
                    for i in range(0, len(bot_stp_nums)):
                        if i > 0:
                            bot_stp_nums[i] -= i
                    for bot_stp_num in bot_stp_nums:
                        bot = core.processes[bot_stp_num]
                        core.stop(bot_stp_num)
                        core.boot(dict(token = bot[0], prefix = bot[1]))
                    ui.sys_message('Successfully restarted the bots')
                else:
                    ui.sys_message('There are no bots running')
            elif choices[choice] == 'Stop Specific':
                core.list_threads()
                if core.processes != []:
                    while True:
                        bot_stp_nums = input('Select the bots you wish to stop by listing the number corrosponding (e.g. 1 2 4): ')
                        bot_stp_nums = bot_stp_nums.split(' ')
                        try:
                            bot_stp_nums = sorted(list(map(int, bot_stp_nums)))
                            break
                        except ValueError as e:
                            print(e)
                    for i in range(0, len(bot_stp_nums)):
                        if i > 0:
                            bot_stp_nums[i] -= i
                    for bot_stp_num in bot_stp_nums:
                        core.stop(bot_stp_num)
                    ui.sys_message('Successfully stopped the bots')
                else:
                    ui.sys_message('There are no bots running')
            elif choices[choice] == 'Quit':
                quit()
        except Exception as e:
            print(f'There has been an error: {e}')
