import subprocess

def install(library_name):
    subprocess.call(f'pip3 install {library_name}', shell=False)
    print(f'Library {library_name} has been installed')

def install_multiple(libraries):
    for library in libraries:
        install(library)

from discord.ext import commands
class Utility(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(
        name='invite',
        help='Generates the link to invite bot',
        pass_context=True
        )
    async def invite(self, ctx):
        await ctx.send(f'https://discord.com/oauth2/authorize?client_id={self.bot.user.id}&scope=bot&permissions=8')

def setup(bot):
    bot.add_cog(Utility(bot))
