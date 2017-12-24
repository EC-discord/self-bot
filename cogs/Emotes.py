import discord
import asyncio
from discord.ext import commands

class Emotes:
     def __init__(self, bot):
          self.bot = bot
     
     @commands.command()
     async def c(self, ctx):
         await ctx.message.edit(content="<:GWmythicalGrandCat:371317556734197761>")  
     
     @commands.command()
     async def m(self, ctx):
         await ctx.message.edit(content="<:GWvictoriaMeguFace:371323891626541057>")
     
     @commands.command()
     async def o(self, ctx):
         await ctx.message.edit(content="<:GWmythicalThonkCool:367331557100224522>")
         
def setup(bot):
    bot.add_cog(Emotes(bot))         
