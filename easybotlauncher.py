#to read savefile
import sqlite3
#discord bot
import discordbot

import pathlib
import os
os.chdir(pathlib.Path(__file__).parent.absolute())

#saving information to database
def save_information(token, prefix):
    conn = sqlite3.connect('save_file.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS saved_information (
        token text,
        prefix text);
        ''')
    conn.commit()
    conn.execute('''INSERT INTO saved_information (token, prefix)
        VALUES (?, ?)''', (token, prefix))
    conn.commit()
    conn.close()

def login(conn):
    #attempt login discord
    cur = conn.cursor()
    cur.execute('SELECT token, prefix FROM saved_information;')
    saved_information_tuple = cur.fetchone()
    discordbot.startup(saved_information_tuple[0], saved_information_tuple[1])

def no_gui_boot():
    #main script UI
    conn = sqlite3.connect('save_file.db')
    try:
        #attempt login discord
        login(conn)
    except:
        token = input('Token: ')
        token = input('Prefix: ')
        save_information(token, prefix)
        discordbot.startup(token, prefix)

#main script UI
conn = sqlite3.connect('save_file.db')
#ui
try:
    from tkinter import *
    try:
        #attempt login discord
        login(conn)
    except sqlite3.Error:
        #upon error start ui
        #window
        tkWindow = Tk()  
        tkWindow.geometry('400x150')  
        tkWindow.title('easybot.py by Chisaki-Dev')
        
        #token label and text entry box
        tokenLabel = Label(tkWindow, text="token").grid(row=0, column=0)
        token = StringVar()
        tokenEntry = Entry(tkWindow, textvariable=token).grid(row=0, column=1)
        tokenLabel = Label(tkWindow, text="You can get this from the discord developers portal").grid(row=0, column=2)

        prefixLabel = Label(tkWindow, text="prefix").grid(row=2, column=0)
        prefix = StringVar()
        prefixEntry = Entry(tkWindow, textvariable=prefix).grid(row=2, column=1)
        prefixLabel = Label(tkWindow, text="This will be what you put before you execute a command").grid(row=2, column=2)

        #startup button
        startupButton = Button(tkWindow, text="start easybot.py", command=lambda:[tkWindow.withdraw(), save_information(token.get(), prefix.get()), discordbot.startup(token.get(), prefix.get())]).grid(row=6, column=1)  

        tkWindow.mainloop()
except:
    print('Will commence non-gui boot...')
    no_gui_boot()