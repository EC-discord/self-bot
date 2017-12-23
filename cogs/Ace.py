import discord
import asyncio
from discord.ext import commands

class Ace: 
     def __init__(self, bot):
          self.bot = bot
    
@commands.command()
async def r(self,ctx):
    await ctx.message.send("t!rep 394111231474270208")

@commands.command()
async def d(self,ctx):
    await ctx.message.send("t!daily 394111231474270208")
    
def setup(bot):
    bot.add_cog(Ace(bot))

    
    
