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
     async def t(self,ctx):
         self.bg_task = self.loop.create_task(self.t())
         await self.wait_until_ready()
         channel = self.get_channel(385439832362582027) # channel ID goes he
         await channel.send("t!fish")
         await asyncio.sleep(30)
    
def setup(bot):
    bot.add_cog(Ace(bot))
