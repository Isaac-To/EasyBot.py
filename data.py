#built in
from json import loads, dumps
def save(tk, px):
    #saves bot to file
    bot_save = open('./data/bots.easybot',"a")
    save_dict = dict(token=tk, prefix=px)
    bot_save.write(f'{dumps(save_dict)}\n')
    bot_save.close()

def extract():
    #extract token/prefix dicts
    bot_save = open('./data/bots.easybot', "r")
    bots = bot_save.readlines()
    bots = [loads(s.replace('\n', '')) for s in bots]
    bot_save.close()
    return bots

def extract_tks():
    #extract saved tokens
    bots = extract()
    bots = [s['token'] for s in bots]
    return bots

def remove(line_num):
    #remove bot dict on specified line
    bots = extract()
    del bots[line_num]
    bot_save = open('./data/bots.easybot', "w+")
    bot_save.write('\n'.join(bots))
    bot_save.close()