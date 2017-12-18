import discord
import asyncio
from discord.ext import commands

class EC: 
     def __init__(self, bot):
          self.bot = bot


     @commands.command()
     async def shrug(self, ctx):
         """Shrugs!"""
         await ctx.message.edit(content="¯\\\_(ツ)\_/¯")

     @commands.command()
     async def tflip(self, ctx):
         """Tableflip!"""
         await ctx.message.edit(content='(╯°□°）╯︵ ┻━┻')

     @commands.command()
     async def cool(self, ctx):
         await ctx.message.edit(content="(  * O *  )")

     @commands.command()
     async def lenny(self, ctx):
         """Lenny Face!"""
         await ctx.message.edit(content="( ͡° ͜ʖ ͡°)")
    
     @commands.command()
     async def gib(self, ctx):
         await ctx.message.edit(content="(づ｡◕‿‿◕｡)づ")
     
     @commands.command()
     async def kflip(self, ctx):
         await ctx.message.edit(content="(づ｡◕‿‿◕｡)づ︵ ┻━┻")
     
     @commands.command()
     async def thumbs(self, ctx):
         await ctx.message.edit(content="( 👍 ' - ') 👍")
     
     @commands.command()
     async def warp(self, ctx):
         await ctx.message.edit(content="(   ' - ')__ (warp drive)")
    
     @commands.command()
     async def hi(self, ctx):
         await ctx.message.edit(content="(  ^ - ^)/")
     
     @commands.command()
     async def ghost(self, ctx):
         await ctx.message.edit(content="〜(  ' - '  )〜")
     
     @commands.command()
     async def wow(self, ctx):
         await ctx.message.edit(content="(   ' O ')")
     
     @commands.command()
     async def noble(self, ctx):
         await ctx.message.edit(content="(  . - .  ) i am noble!")
     
def setup(bot):
    bot.add_cog(EC(bot))
