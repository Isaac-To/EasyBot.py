import subprocess
import os
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
