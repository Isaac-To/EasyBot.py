# built in
import logging
import os
import sqlite3
# self
import core

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    conn = sqlite3.connect('./data/bot.db')
    curr = conn.cursor()
    curr.execute('SELECT * FROM bot')
    tokens = curr.fetchall()
    for token in tokens:
        core.boot(token)
