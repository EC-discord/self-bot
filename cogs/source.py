import discord
from discord.ext import commands
import inspect

class source(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def source(self, ctx, *, command: str):
        """shows source code of a command
        Parameters
        • command - the name of the command for which to display the source code
        """
        nl = "```"
        source_thing = inspect.getsource(self.bot.get_command(command).callback)
        await ctx.send(f"{nl}py\n{source_thing}{nl}")
        
def setup(bot):
    bot.add_cog(source(bot))
