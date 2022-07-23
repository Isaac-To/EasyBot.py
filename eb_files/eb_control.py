#built in
from sys import argv
from os import path, chdir, mkdir
import sqlite3
#self
import ui, core

def offset(list):
    for i in range(0, len(list)):
        if i > 0:
            list[i] -= i
    return list

def inputs():
    while True:
        nums = better.input('Select the bots you wish to select by listing the number corrosponding (e.g. 1 2 4): ').split(' ')
        try:
            nums = sorted(list(map(int, nums)))
            break
        except ValueError as e:
            print(e)
    return nums

class better:
    input_called = -1
    try:
        input_commands = [c.replace('\n', '') for c in open(argv[1], 'r').readlines() if not c.startswith('#')]
    except:
        input_commands = []
    def input(*string):
        if string:
            print(string[0], end='')
        better.input_called += 1
        try:
            print(better.input_commands[better.input_called], end='')
            return better.input_commands[better.input_called]
        except:
            return input()
class commands:
    def help():
        ui.sys_message('Commands List')
        ui.list_dict(choices)
    def add(prefix, token):
        con = sqlite3.connect("./data/bots.db")
        con.execute("INSERT INTO bots (prefix, token) VALUES (?, ?)", (prefix, token))
        con.commit()
        con.close()
    def delete(id):
        con = sqlite3.connect("./data/bots.db")
        con.execute("DELETE FROM bots WHERE id = ?", id)
        con.commit()
        con.close()
    def list_bots():
        con = sqlite3.connect("./data/bots.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM bots ORDER BY id")
        output = cur.fetchall()
        output = [f"{str(o)}\n" for o in output]
        print(''.join(output))
        cur.close()
        con.close()
    def boot(id):
        con = sqlite3.connect("./data/bots.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM bots WHERE id = ?", id)
        toboot = cur.fetchone()
        core.boot(toboot[1], toboot[2])
        cur.close()
        con.close()
    def bootall():
        con = sqlite3.connect("./data/bots.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM bots")
        for toboot in cur.fetchall():
            core.boot(toboot[1], toboot[2])
            cur.close()
    def install():
        from wget import download
        while True:
            link = input("Link: ")
            if link.endswith('.py'):
                download(f'{link}', f'{path.dirname(path.abspath(__file__))}/cogs')
                break
    def running():
        ui.sys_message("Currently active")
        ui.num_list(core.processes)
    def restart():
        core.list_threads()
        if core.processes != []:
            bot_stp_nums = inputs()
            for bot_stp_num in offset(bot_stp_nums):
                bot = core.processes[bot_stp_num]
                core.stop(bot_stp_num)
                core.boot(bot[1], bot[0])
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
    chdir(path.dirname(path.abspath(__file__)))
    try:
        mkdir('./data')
    except: pass
    try:
        mkdir('./cogs')
    except: pass
    con = sqlite3.connect("./data/bots.db")
    con.execute("CREATE TABLE IF NOT EXISTS bots (id INTEGER PRIMARY KEY AUTOINCREMENT, prefix STRING, token STRING)")
    con.commit()
    con.close()
    choices = {
    'add': 'Add bot(s)',
    'delete': 'Remove bot token',
    'bootall':'Boot all',
    'boot': 'Boot specific',
    'listbots': 'Shows all stored bots',
    'install': 'Installs cog from link',
    'kill': 'Stop Specific',
    'running': 'Shows running bots',
    'restart': 'Restart Specific',
    'quit': 'Quit'
    }
    i = 1
    ui.sys_message('EasyBot.py is running')
    while True:
        try:
            commands.help()
            ui.sys_message('Run your commands below')
            choice = better.input()
            if choice == 'add':
                commands.add(better.input('prefix: '), better.input('token: '))
            elif choice == 'delete':
                commands.list_bots()
                commands.delete(better.input('id: '))
            elif choice == 'bootall':
                commands.bootall()
            elif choice == 'boot':
                commands.list_bots()
                commands.boot(better.input('id: '))
            elif choice == 'listbots':
                commands.list_bots()
            elif choice == 'install':
                commands.install()
            elif choice == 'running':
                commands.running()
            elif choice == 'restart':
                commands.restart()
            elif choice == 'kill':
                commands.kill()
            elif choice == 'quit':
                commands.quit()
            else:
                print(f"{choice} is not a proper command")
        except Exception as e:
            print(f'There has been an error: {e}')