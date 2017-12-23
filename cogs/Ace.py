import discord
import asyncio
from discord.ext import commands

class Ace: 
     def __init__(self, bot):
          self.bot = bot
    
     @commands.command()
     async def r(self,ctx):
         await ctx.send("t!rep @Zirus👑#8872")

     @commands.command()
     async def d(self,ctx):
         await ctx.send("t!daily @Zirus👑#8872")
     
     @commands.command()
     async def t(self,ctx):
         await ctx.send("t!fish")
    
def setup(bot):
    bot.add_cog(Ace(bot))
