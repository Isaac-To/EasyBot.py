# Easy-Bot.py
**Easy-Bot.py is a simple and no fuss discord bot starter kit** that you can set up **without** any code. Just drag and drop whatever you want and Easy-Bot.py will try it's best to run it! Easy-Bot's set up is simple with a basic ui that remembers the discord token and prefix so you don't have to!
It supports **multiple** bots in one configuration. This way you can launch multiple bots with the exact same plugin set up so that you can get around the 100 servers limit.

## INSTALL STEPS
Easy-Bot.py REQUIRES PYTHON 3.6+ to be installed (DEVELOPED ON PYTHON 3.9).

The only library this uses is the Discord Library (Which will be automatically installed when eb_launcher.py is run)
However, plugin requirements may vary and require external libraries to be installed but will be attempted to be automatically detected and installed.

## HOW TO USE

### To start the bot
Just execute eb_launcher.py; Launching methods vary depending on system. In most cases, this is in the form of "python3 eb_launcher.py".
#### To start the bot in an isolated enviroment
You can use the start.bat script included to run the Easy-Bot.py. This uses pipenv to isolate the libraries to the enviroment.
### To install a plugin
To install a plugin, simply drag the .py file into the cogs folder and the bot will attempt to run it on the next boot!
By default, a plugin called plugintool is included which a couple basic commands such as invite. This is used to generate a link and qr to invite the bot to another server.
Plugintools also includes functions that can be used by other plugins to simplify the creation of plugin creation.
**"Official" plugins can be found by looking at my other repositories that are labeled "Easy-Bot".**

### To make your own plugin
Check out example_plugin.pyexample. It includes the basic outline of how your should structure your plugin. This is based on discord.py's cog structure.

### To remove a plugin
Just drag/delete the plugin's .py file out of the cogs folder and it will not be loaded up upon the next boot!

## Terms
By using this program, you hereby agree to the terms of the license agreement included.

Updated by chisaku-dev on 07/06/2021
