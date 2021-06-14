# Easy-Bot.py
**Easy-Bot.py is a simple and no fuss discord bot starter kit** that you can set up **without** any code. Just drag and drop whatever you want and Easy-Bot.py will try it's best to run it! Easy-Bot's set up is simple with a basic ui that remembers the discord token and prefix so you don't have to!
It supports **multiple** bots in one configuration. This way you can launch multiple bots with the exact same plugin set up so that you can get around the 100 servers limit.

## INSTALL STEPS
Easy-Bot.py REQUIRES PYTHON 3.6+ to be installed (DEVELOPED ON PYTHON 3.9).

The only library this uses is the Discord Library (install this with pip install discord)
However, plugin requirements may vary and require external libraries to be installed.

## HOW TO USE

### To start the bot
Just execute eb_launcher.py; Launching methods vary depending on system. In most cases, this is in the form of "python3 eb_launcher.py".

### To install a plugin
To install a plugin, simply drag the .py file into the cogs folder and the bot will attempt to run it on the next boot!
By default, a plugin called invitation is included which has the command invite. This is used to generate a link to invite the bot to another server.
**"Official" plugins can be found by looking at my other repositories that are labeled "Easy-Bot".**

## To make your own plugin
Check out example_plugin.pyexample. It includes the basic outline of how your should structure your plugin. This is based on discord.py's cog structure.

### To remove a plugin
Just drag/delete the plugin's .py file out of the cogs folder and it will not be loaded up upon the next boot!

## Terms
By using this program, you hereby agree to the terms of the license agreement included.

Updated by chisaku-dev on 6/13/2021
