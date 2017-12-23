import discord
import asyncio
from discord.ext import commands

class EC: 
     def __init__(self, bot):
          self.bot = bot


     @commands.command()
     async def shrug(self, ctx):
         """¯\\_(ツ)_/¯"""
         await ctx.message.edit(content="¯\\\_(ツ)\_/¯")

     @commands.command()
     async def tflip(self, ctx):
         """(╯°□°）╯︵ ┻━┻"""
         await ctx.message.edit(content='(╯°□°）╯︵ ┻━┻')

     @commands.command()
     async def cool(self, ctx):
         """(  * O *  )"""
         await ctx.message.edit(content="(  * O *  )")

     @commands.command()
     async def lenny(self, ctx):
         """( ͡° ͜ʖ ͡°)"""
         await ctx.message.edit(content="( ͡° ͜ʖ ͡°)")
    
     @commands.command()
     async def gib(self, ctx):
         """(づ｡◕‿‿◕｡)づ"""
         await ctx.message.edit(content="(づ｡◕‿‿◕｡)づ")
     
     @commands.command()
     async def kflip(self, ctx):
         """(づ｡◕‿‿◕｡)づ︵ ┻━┻"""
         await ctx.message.edit(content="(づ｡◕‿‿◕｡)づ︵ ┻━┻")
     
     @commands.command()
     async def thumbs(self, ctx):
         """(👍 ' - ')👍"""
         await ctx.message.edit(content="(👍 ' - ')👍")
     
     @commands.command()
     async def warp(self, ctx):
         """(   ' - ')__(warp drive)"""
         await ctx.message.edit(content="(   ' - ')__(warp drive)")
    
     @commands.command()
     async def hi(self, ctx):
         """(  ^ - ^)/"""
         await ctx.message.edit(content="(  ^ - ^)/")
     
     @commands.command()
     async def ghost(self, ctx):
         """〜(  ' - '  )〜"""
         await ctx.message.edit(content="〜(  ' - '  )〜")
     
     @commands.command()
     async def wow(self, ctx):
         """(   ' O ')"""
         await ctx.message.edit(content="(   ' O ')")
     
     @commands.command()
     async def noble(self, ctx):
         """(  . - .  ) i am noble!"""
         await ctx.message.edit(content="(  . - .  ) i am noble!")
          
     @commands.command()
     async def cookie(self, ctx):
         """(  ^ - ^)-🍪"""
         await ctx.message.edit(content="(  ^ - ^)-🍪")
          
     @commands.command()
     async def cat(self, ctx):
         await ctx.message.edit(content="""{ \  / }
( ^ - ^ )
( u   u )～""")
     
     
def setup(bot):
    bot.add_cog(EC(bot))
