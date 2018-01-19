import discord
import asyncio
from discord.ext import commands

class skid: 
     def __init__(self, bot):
          self.bot = bot
     
     @commands.command()
     async def type(self, ctx, message):
         while True:
             await ctx.message.delete()
             await ctx.channel.trigger_typing()
             if message.content.startswith("=br"):
                 await ctx.message.delete()
                 break
     
def setup(bot):
   bot.add_cog(skid(bot))     
