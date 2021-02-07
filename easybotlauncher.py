#ui
from tkinter import *
#to read savefile
import sqlite3
#discord bot
import discordbot

#saving information to database
def save_information(name, token, prefix):
    conn = sqlite3.connect('save_file.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS saved_information (
        name text,
        token text,
        prefix text);
        ''')
    conn.commit()
    conn.execute('''INSERT INTO saved_information (name, token, prefix)
        VALUES (?, ?, ?)''', (name, token, prefix))
    conn.commit()
    conn.close()

#main script
conn = sqlite3.connect('save_file.db')
try:
    #attempt login discord
    cur = conn.cursor()
    cur.execute('SELECT name, token, prefix FROM saved_information;')
    saved_information_tuple = cur.fetchone()
    discordbot.startup(saved_information_tuple[0], saved_information_tuple[1], saved_information_tuple[2])
    #conn.close()
except sqlite3.Error:
    #upon error start ui
    #window
    tkWindow = Tk()  
    tkWindow.geometry('400x150')  
    tkWindow.title('easybot.py by Chisaki-Dev')
    #name label and text entry box
    nameLabel = Label(tkWindow, text="name").grid(row=0, column=0)
    name = StringVar()
    nameEntry = Entry(tkWindow, textvariable=name).grid(row=0, column=1)  

    #token label and text entry box
    tokenLabel = Label(tkWindow, text="token").grid(row=1, column=0)
    token = StringVar()
    tokenEntry = Entry(tkWindow, textvariable=token).grid(row=1, column=1)  

    prefixLabel = Label(tkWindow, text="prefix").grid(row=4, column=0)
    prefix = StringVar()
    prefixEntry = Entry(tkWindow, textvariable=prefix).grid(row=4, column=1)

    #startup button
    startupButton = Button(tkWindow, text="start easybot.py", command=lambda:[tkWindow.withdraw(), save_information(name.get(), token.get(), prefix.get()), discordbot.startup(name.get(), token.get(), prefix.get())]).grid(row=6, column=1)  

    tkWindow.mainloop()