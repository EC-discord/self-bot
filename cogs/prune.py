import discord
from discord.ext import commands

class prune(object):
    def __init__(self, bot):
        self.bot = bot
        self.server = self.bot.get_guild(268597766652035072)
        self.channel = self.bot.get_channel(477902596397465603)
         
    async def on_message(self, self.channel.message):
            await message.channel.prune()
            
def setup(bot):
    bot.add_cog(prune(bot))
