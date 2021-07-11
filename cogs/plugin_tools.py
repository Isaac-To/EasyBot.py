import subprocess
import os
from discord import file
import qrcode

def install(library_name):
    subprocess.call(f'pip3 install {library_name}', shell=False)
    print(f'Library {library_name} has been installed')

def install_multiple(libraries):
    for library in libraries:
        install(library)

from discord.ext import commands
import discord
class Utility(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
            
    @commands.command(
        name='invite',
        help='Generates the link to invite bot',
    )
    async def invite(self, ctx):
        link = f'https://discord.com/oauth2/authorize?client_id={self.bot.user.id}&scope=bot&permissions=8'
        if not os.path.isfile('./cogs/plugintool/invite.png'):
            img = qrcode.make(link)
            img.save('./cogs/plugintool/invite.png')
        file = discord.File('./cogs/plugintool/invite.png')
        embed = discord.Embed()
        embed.title = f'Invite {self.bot.user.name}'
        embed.description = link
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_image(url='attachment://invite.png')
        await ctx.send(embed=embed, file=file)

    @commands.command(
        name='ping',
        help='Test the latency of the bot'
    )
    async def ping(self, ctx):
        ctx.send(f'Pong took {self.bot.latency} seconds 🏓')

    @commands.command(
        name='serverinfo',
        help='Outputs known server information'
    )
    async def serverinfo(self, ctx):
        guild = ctx.guild
        name = guild.name
        id = guild.id
        channels = guild.channels
        members = guild.member_count
        premium_members = guild.premium_subscription_count
        max_members = guild.max_members
        location = guild.region
        epox = guild.created_at
        owner = guild.owner_id
        explicit = guild.explicit_content_filter
        embed = discord.Embed()
        embed.title = f'Server Info'
        embed.description = f'''
        Name: {name}\n
        ID: {id}\n
        # of channels: {len(channels)}\n
        # of nitro boosted members: {premium_members}\n
        # of members: {members}/{max_members}\n
        Located in {location}\n
        Created on {epox}\n
        Owned by UID: {owner}\n
        Explicit content filter enabled for {explicit}\n
        '''
        embed.set_thumbnail(url=guild.icon_url)
        await ctx.send(embed=embed)

class Misc(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
            
    @commands.command(
        name='makeyourownbot',
        help='Make your own discord bot with EasyBot framework by Chisaku-Dev'
    )
    async def makeyourownbot(self, ctx):
        link = f'https://github.com/chisaku-dev/EasyBot.py'
        if not os.path.isfile('./cogs/plugintool/makeyourownbot.png'):
            img = qrcode.make(link)
            img.save('./cogs/plugintool/makeyourownbot.png')
        file = discord.File('./cogs/plugintool/makeyourownbot.png')
        embed = discord.Embed()
        embed.title = f'Make a bot like {self.bot.user.name}!'
        embed.description = link
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_image(url='attachment://makeyourownbot.png')
        await ctx.send(embed=embed, file=file)

def setup(bot):
    bot.add_cog(Utility(bot))
    bot.add_cog(Misc(bot))
