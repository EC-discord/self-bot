import discord
import asyncio
from discord.ext import commands

class Ace: 
     def __init__(self, bot):
          self.bot = bot
    
     @commands.command()
     async def r(self,ctx):
         await ctx.send("t!rep <@264634027280039938>")

     @commands.command()
     async def d(self,ctx):
         await ctx.send("t!daily <@264634027280039938>")
     
     @commands.command()
     async def t(self, ctx):
         while True:
             await asyncio.sleep(30)
             channel = self.get_channel(385439832362582027)
             await channel.send("t!fish")
    
def setup(bot):
    bot.add_cog(Ace(bot))
