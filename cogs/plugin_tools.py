import subprocess
import os
import qrcode
import image

def install(library_name):
    subprocess.call(f'pip3 install {library_name}', shell=False)
    print(f'Library {library_name} has been installed')

def install_multiple(libraries):
    for library in libraries:
        install(library)

def is_op(uid):
    print(f'If you triggered this command, copy {uid} to ops in the cog/plugintool/ folder and rerun again. Otherwise, just ignore this message')
    op = open('./cogs/plugintool/ops', 'r')
    ops = op.readlines()
    if str(uid) in ops:
        return True
    else:
        return False

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
        await ctx.send(f'Pong took {self.bot.latency} seconds 🏓')

    @commands.command(
        name='serverinfo',
        help='Known server information'
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

    @commands.command(
        name='botinfo',
        help='Statistics about this bot'
    )
    async def botinfo(self, ctx):
        bot = self.bot
        name = bot.user.name
        id = bot.user.id
        guilds = bot.guilds
        total_members = 0
        for guild in guilds:
            total_members += guild.member_count
        average_members_per_guild = total_members / len(guilds)
        embed = discord.Embed()
        embed.title = f'Bot Info'
        embed.description = f'''
        Name: {name}\n
        ID: {id}\n
        Servers: {len(guilds)}\n
        Total Users: {total_members}\n
        Average Users Per Server: {average_members_per_guild}\n
        '''
        embed.set_thumbnail(url=bot.user.avatar_url)
        await ctx.send(embed=embed)

class Bot_Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.is_owner()
    @commands.command(
        name='botgrowth',
        help='Tips based on bot statistics on how to reach more people!'
    )
    async def botgrowth(self, ctx):
        await ctx.send('Unfinished')

    @commands.is_owner()
    @commands.command(
        name='prune',
        help='Removes bot from servers smaller than the specified limit'
    )
    async def purge(self, ctx, minimum):
        guilds_left = 0
        embed = discord.Embed()
        embed.title = 'Notice of Leave'
        embed.description = f'''{self.bot.user.name} will be leaving your server due to a lack of users;\n
        This is done to ensure the bot can reach as many people as possible as discord limits the amount of servers one bot can be in to 100.\n
        This limit is out of our control and the best solution is to trim down the number of smaller servers such that more people can enjoy this bot\n
        It's been a joy working with you and your patrons!\n
        If you wish to invite me again, use https://discord.com/oauth2/authorize?client_id={self.bot.user.id}&scope=bot&permissions=8\n\n\n
        \tMay we meet again soon,\n
        {self.bot.user.name}'''
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        for guild in self.bot.guilds:
            if guild.member_count < int(minimum):
                for channel in guild.channels:
                    try:
                        await channel.send(embed=embed)
                        break
                    except: pass
                guilds_left += 1
                await guild.leave()
        await ctx.send(f"Left {guilds_left} server(s)!")

    @commands.is_owner()
    @commands.command(
        name="broadcast",
        help="Sends a broadcast to all servers this bot is connected to; Only use this for serious messages!"
    )
    async def broadcast(self, ctx):
        def check(ms):
            return ms.channel == ctx.message.channel and ms.author == ctx.message.author
        await ctx.send('Enter your message:')
        msg = await self.bot.wait_for('message', check=check)
        embed = discord.Embed()
        embed.title = f'{self.bot.user.name} Admin Broadcast'
        embed.description = msg.content
        for guild in self.bot.guilds:
            for channel in guild.channels:
                try:
                    await channel.send(embed=embed)
                    break
                except: pass
        await ctx.send(f"Message broadcasted to all servers connected")

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
    bot.add_cog(Bot_Admin(bot))
