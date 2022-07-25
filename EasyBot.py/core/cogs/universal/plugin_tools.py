#built in
import os

def discord_colors():
    colors = [0x8B77BE, 0xA189E2, 0xCF91D1, 0x5665AA, 0xA3A3D2]
    from random import choice
    return choice(colors)

def install(library_name):
    os.system(f'pip3 install {library_name}')
    print(f'Library {library_name} has been installed')

def install_multiple(libraries):
    for library in libraries:
        install(library)

def fast_embed(content):
    return disnake.Embed(description=content, color=discord_colors())

from disnake.ext import commands
import disnake
class PUtility(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(description="Creates invite link for bot")
    async def invite(self, inter):
        embed = disnake.Embed(color=discord_colors())
        embed.title = f'Invite {self.bot.user.name}'
        embed.description = f'https://discord.com/oauth2/authorize?client_id={self.bot.user.id}&scope=bot&permissions=8'
        if self.bot.user.avatar != None:
            embed.set_thumbnail(url=self.bot.user.avatar)
        await inter.response.send_message(embed=embed)

    @commands.slash_command(description="Pings the bot")
    async def ping(self, inter):
        await inter.response.send_message(embed=fast_embed(f'Pong took {self.bot.latency} seconds 🏓'))

    @commands.slash_command(description="Provides information on the bot")
    async def botinfo(self, inter):
        bot = self.bot
        name = bot.user.name
        id = bot.user.id
        guilds = bot.guilds
        total_members = 0
        for guild in guilds:
            total_members += guild.member_count
        average_members_per_guild = total_members / len(guilds)
        embed = disnake.Embed(color=discord_colors())
        embed.title = f'Bot Info'
        embed.description = f'''
        Name: {name}\n
        ID: {id}\n
        Servers: {len(guilds)}\n
        Total Users: {total_members}\n
        Average Users Per Server: {average_members_per_guild}\n
        '''
        if self.bot.user.avatar != None:
            embed.set_thumbnail(url=self.bot.user.avatar)
        await inter.response.send_message(embed=embed)

class Bot_Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Provides information on how to improve your bot's reach")
    async def botgrowth(self, inter):
        total_users = 0
        for guild in self.bot.guilds:
            total_users += guild.member_count
        total_guilds = len(self.bot.guilds)
        embed = disnake.Embed(color=discord_colors())
        embed.title = f'Tips'
        if self.bot.user.avatar != None:
            embed.set_thumbnail(url=self.bot.user.avatar)
        if total_guilds > 75:
            if total_users/total_guilds > 150:
                embed.description = '''
                You have good server densities on this bot which means that it isn't worth trimming as there just isn't enough small servers to make a noticable difference.\n
                - You can try to verify your bot with discord which means providing your ID to bypass the 100 server limit.
                - Or you can add another bot to function as a clone of this bot through the launcher with the add command.
                '''
            else:
                embed.description = '''
                Your server density is still quite low on this bot which means trimming smaller servers can make space to reach more users
                - You should try using the prune command to trim smaller servers. A size of 5-10 can help ensure that you have enough space in your server limits
                - Alternatively you can verify your bot with discord which means providing your ID to bypass the 100 server limit.
                '''
        else:
            embed.description = '''
            Your bot is stil relatively small and has space to grow.
            - You should try advertising your bot on bot finder pages like top.gg to get more attention.
            - Also try inviting your friends to invite this bot to their servers as well!
            The more popular your bot is, the more people that will use it!'''
            if total_users/total_guilds < 50:
                embed.description += '''\nAdditionally, your server density is still fairly low
                - If the theme of the bot matches try asking owners of larger servers to invite your bot!'''
        await inter.response.send_message(embed=embed)


    @commands.slash_command(description="Removes small servers from the bot")
    async def purge(self, inter, minimum):
        guilds_left = 0
        embed = disnake.Embed(color=discord_colors())
        embed.title = 'Notice of Leave'
        embed.description = f'''{self.bot.user.name} will be leaving your server due to a lack of users;
        This is done to ensure the bot can reach as many people as possible as discord limits the amount of servers one bot can be in to 100.
        This limit is out of our control and the best solution is to trim down the number of smaller servers such that more people can enjoy this bot
        It's been a joy working with you and your patrons!
        If you wish to invite me again, use https://discord.com/oauth2/authorize?client_id={self.bot.user.id}&scope=bot&permissions=8\n\n\n
        \tMay we meet again soon,
        {self.bot.user.name}'''
        if self.bot.user.avatar != None:
            embed.set_thumbnail(url=self.bot.user.avatar)
        for guild in self.bot.guilds:
            if guild.member_count < int(minimum):
                for channel in guild.channels:
                    try:
                        await channel.response.send_message(embed=embed)
                        break
                    except: pass
                guilds_left += 1
                await guild.leave()
        await inter.response.send_message(f"Left {guilds_left} server(s)!")

    @commands.is_owner()
    @commands.slash_command(description="Sends message to every server this bot is in")
    async def broadcast(self, inter):
        def check(ms):
            return ms.channel == inter.message.channel and ms.author == inter.message.author
        await inter.response.send_message('Enter your message:')
        msg = await self.bot.wait_for('message', check=check)
        embed = disnake.Embed(color=discord_colors())
        embed.title = f'{self.bot.user.name} Admin Broadcast'
        embed.description = msg.content
        if self.bot.user.avatar != None:
            embed.set_thumbnail(url=self.bot.user.avatar)
        for guild in self.bot.guilds:
            for channel in guild.channels:
                try:
                    await channel.response.send_message(embed=embed)
                    break
                except: pass
        await inter.response.send_message(f"Message broadcasted to all servers connected")

def setup(bot):
    bot.add_cog(PUtility(bot))
    bot.add_cog(Bot_Admin(bot))
