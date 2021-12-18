#discord
from discord import Embed, Activity, ActivityType
from discord.ext import commands
#built in
from time import strftime, localtime
from os import chdir, path, listdir, mkdir, system
#self
import ui

async def cog(client):
#cogs detection
    chdir(path.dirname(path.abspath(__file__)))
    cogs = [f[:-3] for f in listdir('./cogs') if f.endswith('.py')]
    if len(cogs) >= 5:
        print('This may take a while... please wait patiently')
    for cog in cogs:
        install = False
        while True:
            try:
                try:
                    mkdir(f'./cogs/{cog}', mode = 0o666)
                except: pass
                client.load_extension(f'cogs.{cog}')
                print(f'{cog} is loaded successfully')
                break
            except commands.ExtensionAlreadyLoaded:
                print(f'{cog} is already loaded; There may be a duplicate file or another version present')
                break
            except Exception as e:
                e = str(e)
                if 'ModuleNotFoundError' in e or install != True:
                    library_name = e[(72 + len(cog)):].replace("'", "")
                    system(f'pip3 install {library_name}')
                    print(library_name, 'has been attempted to be installed')
                    install = True
                else:
                    print(f'There was an error with {cog} with the error: {e}\n {cog} will be skipped')
                    break

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
    async def on_command_error(ctx, error):
        await ctx.send(error)
    
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