from discord.ext import commands
import discord

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
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

def setup(bot):
    bot.add_cog(Utility(bot))
