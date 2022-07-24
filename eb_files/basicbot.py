#built in
from time import strftime, localtime
from os import chdir, path, listdir, mkdir, system
import logging
#discord
from disnake import Embed, Activity, ActivityType
from disnake.ext import commands

async def cog(client):
#cogs detection
    try:
        mkdir(f'./cogs/{client.user.id}')
    except: pass
    cogs = [f[:-3] for f in listdir(f'./cogs/{client.user.id}') if f.endswith('.py')]
    universal_cogs = [f[:-3] for f in listdir('./cogs/universal') if f.endswith('.py')]
    if len(cogs) >= 5:
        print('This may take a while... please wait patiently')
    for cog in cogs:
        await load_cog(client, f'cogs.{client.user.id}.{cog}')
    for cog in universal_cogs:
        await load_cog(client, f'cogs.universal.{cog}')

async def load_cog(client, path):
    try:
        client.load_extension(path)
        logging.info(f'{path} is loaded successfully')
    except commands.ExtensionAlreadyLoaded:
        logging.error(f'{path} is already loaded; There may be a duplicate file or another version present')
    except Exception as e:
        logging.error(e)

#bot main
def main(token, prefix):
    def __init__(self, client):
        self.client = client
    
    bot = commands.Bot(command_prefix=prefix)

    #embed help command
    class helpcommand(commands.MinimalHelpCommand):
        async def send_pages(self):
            destination = self.get_destination()
            embed = Embed(title='Help', description='', color=0x8B77BE)
            embed.description = '\n'.join(list(self.paginator.pages))
            await destination.send(embed=embed)
    bot.help_command = helpcommand()

    #on boot
    @bot.event
    async def on_ready():
        try:
            mkdir(f'./data/logs', mode = 0o666)
        except: pass
        #ensure file exists for log to be written to
        f = open(f"./data/logs/{bot.user.id}", "w")
        f.close()
        logging.info(f'Booted {bot.user.id}')
        await cog(bot)
        print(f'USN:{bot.user.name}\nUID:{bot.user.id}\nInvite: https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8')
        logging.info(f'USN:{bot.user.name}\nUID:{bot.user.id}\nInvite: https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8')
        presense =  f" {prefix}help"
        await bot.change_presence(activity=Activity (type=ActivityType.watching, name=presense))

    #error response
    @bot.event
    async def on_command_error(inter, error):
        await inter.response.send_message(error)

    #start bot
    try:
        chdir(path.dirname(path.abspath(__file__)))
        logging.basicConfig(filename=f'./logs/{strftime("%Y%m%d%H%M")}.log', encoding='utf-8', level=logging.DEBUG)
        bot.run(token)
    except Exception as e:
        #will state when an invalid token has been used
        logging.error(e)
        return