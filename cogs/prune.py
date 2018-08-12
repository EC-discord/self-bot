import discord
from discord.ext import commands

class prune(object):
    def __init__(self, bot):
        self.bot = bot
        
    async def on_message(self, message):
        if message.channel.id == 477902596397465603:
            await message.channel.prune()
            
def setup(bot):
    bot.add_cog(prune(bot))
