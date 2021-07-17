#discord
import discord
from discord.ext import commands
#built in
import os, time
#self
import ui

async def cog(client):
#cogs detection
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    cogs = [f for f in os.listdir('./cogs') if f.endswith('.py')]
    if len(cogs) >= 5:
        print('This may take a while... please wait patiently')
    for cog in cogs:
        cog = cog.replace('.py', '')
        while True:
            try:
                try:
                    os.mkdir(f'./cogs/{cog}', mode = 0o666)
                except: pass
                client.load_extension(f'cogs.{cog}')
                print(f'{cog} is loaded successfully')
                break
            except discord.ext.commands.ExtensionAlreadyLoaded:
                print(f'{cog} is already loaded; There may be a duplicate file or another version present')
                break
            except Exception as e:
                e = str(e)
                if 'ModuleNotFoundError' in e:
                    library_name = e[(72 + len(cog)):].replace("'", "")
                    os.system(f'pip3 install {library_name}')
                    print(library_name, 'has been installed')
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
            embed = discord.Embed(title='Help', description='')
            embed.description = '\n'.join(list(self.paginator.pages))
            await destination.send(embed=embed)
    bot.help_command = helpcommand()

    #on boot
    @bot.event
    async def on_ready():
        ui.sys_message('Successfully booted')
        await cog(bot)
        print(f'USN:{bot.user.name}\nUID:{bot.user.id}\nInvite: https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8 \n')
        presense =  f" your call using {prefix}"
        if prefix.endswith(' '):
            presense = presense[:-1] + f'; Note: there is a space following {prefix[:-1]}'
        await bot.change_presence(activity=discord.Activity (type=discord.ActivityType.listening, name=presense))

    #error response
    @bot.event
    async def on_command_error(ctx, error):
        await ctx.send(error)

    @bot.event
    async def on_message(message):
        msg = str(message.content).lower()
        if msg.startswith(prefix) and message.author != bot.user:
            print(time.strftime("%H:%M:%S", time.localtime()), bot.user.id, message.content)
            message.content = str(message.content).lower()
            await bot.process_commands(message)

    #start bot
    try:
        bot.run(token)
    except Exception as e:
        #will state when an invalid token has been used
        ui.sys_message(e)
        return