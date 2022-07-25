import sqlite3
import os

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    folders = ['./logs', './data']
    # create folders
    for fo in folders:
        try:
            os.mkdir(fo)
        except: pass
    conn = sqlite3.connect('./data/bot.db')
    conn.execute('CREATE TABLE IF NOT EXISTS bot (token TEXT)')
    conn.commit()
    conn.close()
    print('Database was created')