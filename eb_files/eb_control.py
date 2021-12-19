#built in
from sys import argv
from os import path, chdir, mkdir
#self
import ui, core
from sqlalchemy import Column, MetaData, String, Table, create_engine, Integer, insert, select

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
        meta = MetaData()
        engine = create_engine('sqlite:///data/bots.db')
        conn = engine.connect()
        ins = insert(Column('prefix', String), Column('token', String)).values(prefix=prefix, token=token)
        conn.execute(ins)
        conn.close()
    def delete(id):
        meta = MetaData()
        engine = create_engine('sqlite:///data/bots.db')
        bots = Table('bots', meta, Column('id', Integer, primary_key=True, autoincrement=True), Column('prefix', String), Column('token', String))
        delete = bots.delete().where(bots.c.id == id)
        conn = engine.connect()
        conn.execute(delete)
        conn.close()
    def list_bots():
        meta = MetaData()
        engine = create_engine('sqlite:///data/bots.db')
        bots = Table('bots', meta, Column('id', Integer, primary_key=True, autoincrement=True), Column('prefix', String), Column('token', String))
        sel = bots.select().order_by(bots.c.id)
        conn = engine.connect()
        conn.execute(sel)
        output = conn.fetchall()
        output = [f"{str(o)}\n" for o in output]
        print(''.join(output))
        conn.close()
    def boot(id):
        meta = MetaData()
        engine = create_engine('sqlite:///data/bots.db')
        bots = Table('bots', meta, Column('id', Integer, primary_key=True, autoincrement=True), Column('prefix', String), Column('token', String))
        sel = bots.select().where(bots.c.id == id)
        conn = engine.connect()
        conn.execute(sel)
        toboot = conn.fetchone()
        core.boot(toboot[1], toboot[2])
        conn.close()
    def bootall():
        meta = MetaData()
        engine = create_engine('sqlite:///data/bots.db')
        bots = Table('bots', meta, Column('id', Integer, primary_key=True, autoincrement=True), Column('prefix', String), Column('token', String))
        sel = bots.select()
        conn = engine.connect()
        conn.execute(sel)
        results = conn.fetchall()
        for toboot in results:
            core.boot(toboot[1], toboot[2])
        conn.close()
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
    meta = MetaData()
    engine = create_engine("sqlite:///data/bots.db")
    bots = Table('bots', meta, Column('id', Integer, primary_key=True, autoincrement=True), Column('prefix', String), Column('token', String))
    meta.create_all(engine)
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
