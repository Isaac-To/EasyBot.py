#built in
import multiprocessing
import json
#self
import ui
import discordbot as db

class core():
    threads = []

    def boot(bot):
        core.threads.append(multiprocessing.Process(target=db.main, args=(bot['token'], bot['prefix'])))
        core.threads[-1].start()
        return

class data:
    def save(tk, px):
        bot_save = open('./data/bots.easybot',"a")
        save_dict = dict(token=tk, prefix=px)
        bot_save.write(f'{json.dumps(save_dict)}\n')
        bot_save.close()
        return

    def extract():
        bot_save = open('./data/bots.easybot', "r")
        bots = bot_save.readlines()
        bots = [json.loads(s.replace('\n', '')) for s in bots]
        bot_save.close()
        return bots

    def extract_tks():
        bots = data.extract()
        bots = [s['token'] for s in bots]
        return bots
    
    def remove(line_num):
        bots = data.extract()
        del bots[line_num]
        bot_save = open('./data/bots.easybot', "w+")
        bot_save.write('\n'.join(bots))
        bot_save.close()

if __name__ == '__main__':
    bt_threads = []
    while True:
        try:
            choices = ['Add bot(s)', 'Remove bot(s)', 'Boot all', 'Boot specific', 'Start selected', 'Quit']
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
            elif choices[choice] == 'Startup selected':
                core.startup()
            elif choices[choice] == 'Quit':
                quit()
        except:
            print('There has been an error')
