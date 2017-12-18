import discord
import asyncio
from discord.ext import commands

class EC: 
     def __init__(self, bot):
          self.bot = bot


     #@commands.group(invoke_without_command=True)
    # async def lenny(self, ctx):
     #    """group commands"""
     #    msg = 'Available: `{}lenny face`, `{}lenny shrug`, `{}lenny flip`, `{}unflip`, `{}lenny gib`'
      #   await ctx.send(msg.format(ctx.prefix))

     @commands.command()
     async def shrug(self, ctx):
         """Shrugs!"""
         await ctx.message.edit(content='¯\\\_(ツ)\_/¯')

     @commands.command()
     async def tableflip(self, ctx):
         """Tableflip!"""
         await ctx.message.edit(content='(╯°□°）╯︵ ┻━┻')

     @commands.command()
     async def unflip(self, ctx):
         """Unflips!"""
         await ctx.message.edit(content='┬─┬﻿ ノ( ゜-゜ノ)')

     @commands.command()
     async def lenny(self, ctx):
         """Lenny Face!"""
         await ctx.message.edit(content='( ͡° ͜ʖ ͡°)')
    
     @commands.command()
     async def gib(self, ctx):
         await ctx.message.edit(content='(づ｡◕‿‿◕｡)づ')
    
def setup(bot):
    bot.add_cog(EC(bot))
