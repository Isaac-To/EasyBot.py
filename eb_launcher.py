#built in
import multiprocessing
import json
import os
import time
#self
import eb_ui
import basicbot as db

class core():
    threads = []

    def boot(bot):
        core.threads.append((bot['token'], multiprocessing.Process(target=db.main, args=(bot['token'], bot['prefix']))))
        core.threads[-1][1].start()

    def list_threads():
        eb_ui.num_list(core.threads)

    def stop(bot_num):
        core.threads[bot_num][1].terminate()
        core.threads.remove(core.threads[bot_num])

class data:
    def save(tk, px):
        #saves bot to file
        bot_save = open('./data/bots.easybot',"a")
        save_dict = dict(token=tk, prefix=px)
        bot_save.write(f'{json.dumps(save_dict)}\n')
        bot_save.close()

    def extract():
        #extract token/prefix dicts
        bot_save = open('./data/bots.easybot', "r")
        bots = bot_save.readlines()
        bots = [json.loads(s.replace('\n', '')) for s in bots]
        bot_save.close()
        return bots

    def extract_tks():
        #extract saved tokens
        bots = data.extract()
        bots = [s['token'] for s in bots]
        return bots
    
    def remove(line_num):
        #remove bot dict on specified line
        bots = data.extract()
        del bots[line_num]
        bot_save = open('./data/bots.easybot', "w+")
        bot_save.write('\n'.join(bots))
        bot_save.close()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    while True:
        try:
            choices = ['Add bot(s)', 'Remove bot(s)', 'Boot all', 'Boot specific', 'Boot w/o saving token', 'Stop Specific', 'Quit']
            while True:
                eb_ui.num_list(choices)
                try:
                    choice = int(input('Enter the number you wish to execute:\n'))
                    break
                except ValueError as e:
                    eb_ui.sys_message(e)
            if choices[choice] == 'Add bot(s)':
                tks = input('What is your bot token(s) (if multiple, seperate them with spaces)? Obtain it from https://discord.com/developers/ and paste it here: ')
                tks = tks.split(' ')
                for tk in tks:
                    data.save(tk, input('Prefix: '))
                eb_ui.sys_message('Success')
            elif choices[choice] == 'Remove bot(s)':
                bot = data.extract()
                eb_ui.num_list(bot)
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
                    eb_ui.sys_message('Success')
                else:
                    eb_ui.sys_message('There are no bots stored')
            elif choices[choice] == 'Boot all':
                bots = data.extract()
                if bots != []:
                    for bot in bots:
                        core.boot(bot)
                else:
                    eb_ui.sys_message('There are no bots stored')
            elif choices[choice] == 'Boot specific':
                bots = data.extract()
                eb_ui.num_list(bots)
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
                    eb_ui.sys_message('There are no bots stored')
            elif choices[choice] == 'Boot w/o saving token':
                tk = input('What is the bot token?\n')
                px = input('What is the desired bot prefix?\n')
                bot = dict(token = tk, prefix = px)
                core.boot(bot)
            elif choices[choice] == 'Stop Specific':
                core.list_threads()
                if bot != []:
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
                    eb_ui.sys_message('Success')
                else:
                    eb_ui.sys_message('There are no bots running')
            elif choices[choice] == 'Quit':
                os._exit(0)
        except Exception as e:
            print(f'There has been an error: {e}')
