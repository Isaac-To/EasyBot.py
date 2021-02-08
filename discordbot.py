#discord
import discord
from discord.ext import commands

import os
import asyncio

async def cog(bot):
    #refresh cogs
    cogs = [f for f in os.listdir('./cogs') if f.endswith('.py')]
    for cog in cogs:
        cog = cog.replace('.py', '')
        try:
            bot.load_extension(f'cogs.{cog}')
            print(f'{cog} is loaded')
        except discord.ext.commands.ExtensionAlreadyLoaded:
            await asyncio.sleep(0)

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
        print(f'Logged in as {bot.user.name} - {bot.user.id}')
        while True:
            #load all detected cogs
            await cog(bot)
            await bot.change_presence(activity=discord.Activity(
                type = discord.ActivityType.listening,
                name=(f" {len(bot.guilds)} servers!")))
    
    #when bot has a command error
    @bot.event
    async def on_command_error(ctx, error):
        await ctx.send(error)
    
    bot.run(token, bot=True, reconnect=True)