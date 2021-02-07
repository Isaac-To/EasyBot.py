#discord
import discord
from discord.ext import commands

import os
import asyncio

#bot main
def startup(name, token, prefix):
    #start bot
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
    async def on_ready():
        print(f'Logged in as {bot.user.name} - {bot.user.id}')
        #importing all plugins found in cogs folder
        cogs = [f for f in os.listdir('./cogs') if f.endswith('.py')]
        if not len(cogs) == 0:
            for cog in cogs:
                try:
                    print(f'{cog} was detected and initializing')
                    cog = cog.replace('.py', '')
                    bot.load_extension(f'cogs.{cog}')
                except:
                    print(f'There was an error at {cog}')
        else:
            print('No plugins were detected')
        #starting up bot
        while True:
            await bot.change_presence(activity=discord.Activity(
                type = discord.ActivityType.listening,
                name=(f" {len(bot.guilds)} servers!")))
            await asyncio.sleep(60)

    @bot.event
    async def on_command_error(ctx, error):
        await ctx.send(error)
    
    bot.run(token, bot=True, reconnect=True)