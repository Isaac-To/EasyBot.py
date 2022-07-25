import sqlite3
import os
if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    conn = sqlite3.connect('./data/bot.db')
    token = input('Discord bot token: ')
    conn.execute('INSERT INTO bot VALUES (?)', (token,))
    conn.commit()
    conn.close()
