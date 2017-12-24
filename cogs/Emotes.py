import discord
import asyncio
from discord.ext import commands

class Emotes:
     def __init__(self, bot):
          self.bot = bot
     
     @commands.command()
     async def m(self, ctx):
         await ctx.send("<:GWmythicalGrandCat:371317556734197761>")  
         
def setup(bot):
    bot.add_cog(Emotes(bot))         
