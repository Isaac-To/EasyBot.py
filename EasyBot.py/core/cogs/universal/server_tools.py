from disnake.ext import commands
import disnake
from core.cogs.universal import plugin_tools

class SUtility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(description="Provides information on the server")
    async def serverinfo(self, inter):
        guild = inter.guild
        name = guild.name
        id = guild.id
        channels = guild.channels
        members = guild.member_count
        premium_members = guild.premium_subscription_count
        max_members = guild.max_members
        epox = guild.created_at
        owner = guild.owner_id
        explicit = guild.explicit_content_filter
        embed = disnake.Embed(color=plugin_tools.discord_colors())
        embed.title = f'Server Info'
        embed.description = f'''
        Name: {name}\n
        ID: {id}\n
        # of channels: {len(channels)}\n
        # of nitro boosted members: {premium_members}\n
        # of members: {members}/{max_members}\n
        Created on {epox}\n
        Owned by UID: {owner}\n
        Explicit content filter enabled for {explicit}\n
        '''
        if guild.icon != None:
            embed.set_thumbnail(url=guild.icon)
        await inter.response.send_message(embed=embed)

    @commands.slash_command(description="Deletes messages up to the number inputted")
    async def clear(self, inter, number_of_messages: int):
        await inter.channel.purge(limit=number_of_messages + 1)
        deletemessage = await inter.response.send_message(embed=plugin_tools.fast_embed(f'{number_of_messages} messages were deleted'), delete_after = 3)


def setup(bot):
    bot.add_cog(SUtility(bot))
