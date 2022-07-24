#discord
from disnake import Embed, Activity, ActivityType
from disnake.ext import commands
#built in
from time import strftime, localtime
from os import chdir, path, listdir, mkdir, system
#self
import ui

async def cog(client):
#cogs detection
    chdir(path.dirname(path.abspath(__file__)))
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
        print(f'{path} is loaded successfully')
    except commands.ExtensionAlreadyLoaded:
        print(f'{path} is already loaded; There may be a duplicate file or another version present')

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
        ui.sys_message('Booted')
        await cog(bot)
        print(f'USN:{bot.user.name}\nUID:{bot.user.id}\nInvite: https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8')
        ui.sys_message('Run your commands below')
        presense =  f" {prefix}help"
        await bot.change_presence(activity=Activity (type=ActivityType.watching, name=presense))

    #error response
    @bot.event
    async def on_command_error(inter, error):
        await inter.response.send_message(error)
    
    @bot.event
    async def on_message(message):
        msg = str(message.content).lower()
        if msg.startswith(prefix) and message.author != bot.user:
            chdir(path.dirname(path.abspath(__file__)))
            log = open(f"./data/logs/{bot.user.id}", "a")
            log.write(f"{strftime('%H:%M:%S', localtime())}| {message.content}\n")
            log.close()
            message.content = str(message.content[:len(prefix)]).lower() + str(message.content[len(prefix):])
            await bot.process_commands(message)

    #start bot
    try:
        bot.run(token)
    except Exception as e:
        #will state when an invalid token has been used
        ui.sys_message(e)
        return