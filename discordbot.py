#discord
import discord
from discord.ext import commands
#built in
import os
#self
import ui

async def cog(client):
#cogs detection
    cogs = [f for f in os.listdir('./cogs') if f.endswith('.py')]
    for cog in cogs:
        cog = cog.replace('.py', '')
        try:
            client.load_extension(f'cogs.{cog}')
            print(f'{cog} is loaded')
        except discord.ext.commands.ExtensionAlreadyLoaded:
            print(f'{cog} is already loaded; There may be a duplicate file')
        except:
            print(f'There was an error with {cog}')

#bot main
def main(token, prefix):
    def __init__(self, client):
        self.client = client
    
    bot = commands.Bot(command_prefix=prefix)

    #embed help command
    class helpcommand(commands.MinimalHelpCommand):
        async def send_pages(self):
            destination = self.get_destination()
            e = discord.Embed(color=0x1ABC9C, description='')
            for page in self.paginator.pages:
                e.description += page
            await destination.send(embed=e)
    bot.help_command = helpcommand()

    @bot.event
    async def on_ready():
        ui.sys_message('Successfully booted')
        await cog(bot)
        print(f'USN:{bot.user.name}\nUID:{bot.user.id}\nInvite: https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8')
        await bot.change_presence(activity=discord.Activity (type=discord.ActivityType.listening, name=f'you for when you use {prefix}'))
    
    bot.run(token)