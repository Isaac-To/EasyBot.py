#discord
import discord
from discord.ext import commands

import os

async def cog(bot):
    #refresh cogs
    cogs = [f for f in os.listdir('./cogs') if f.endswith('.py')]
    for cog in cogs:
        cog = cog.replace('.py', '')
        try:
            bot.load_extension(f'cogs.{cog}')
            print(f'{cog} is loaded')
        except discord.ext.commands.ExtensionAlreadyLoaded:
            print(f'{cog} is already loaded; There may be a duplicate file')
        except:
            print(f'There was an error with {cog}')
    
async def background_activities(bot):
    await bot.change_presence(activity=discord.Activity(
                type = discord.ActivityType.listening,
                name=("{} servers!").format(len(bot.guilds))))

#bot main
def startup(name, token, prefix):
    #declare bot
    bot = commands.Bot(
        command_prefix=prefix,
        help=f'A {name} bot',
        case_insensitive=True
    )

    #embed help
    class helpcommand(commands.MinimalHelpCommand):
        async def send_pages(self):
            destination = self.get_destination()
            e = discord.Embed(color=0x1ABC9C, description='')
            for page in self.paginator.pages:
                e.description += page
            await destination.send(embed=e)
    bot.help_command = helpcommand()

    @bot.event
    #starting up bot
    async def on_ready():
        await cog(bot)
        print(f'Logged in as {bot.user.name} - {bot.user.id}')
        while True:
            await background_activities(bot)
    
    #when bot has a command error
    @bot.event
    async def on_command_error(ctx, error):
        await ctx.send(error)
    
    bot.run(token, bot=True, reconnect=True)