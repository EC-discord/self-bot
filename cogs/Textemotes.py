import discord
import asyncio
from discord.ext import commands

class Textemotes(commands.Cog): 
     def __init__(self, bot):
          self.bot = bot
          
     @commands.command()
     async def snipe(self, ctx, member: discord.Member = " "):
          member = member or " "
          #if member is None:
          #     await ctx.message.edit(content = '(　-_･) ︻デ═一"    ▸')
          #else:
          await ctx.message.edit(content = f'(　-_･) ︻デ═一"    ▸ {member}')
     
     @commands.command()
     async def thumbs(self, ctx):
         """(👍' - ')👍"""
         await ctx.message.edit(content="(👍' - ')👍")
          
     @commands.command()
     async def cookie(self, ctx):
         """(  ' - ')-🍪"""
         await ctx.message.edit(content="(  ' - ')-🍪")
          
     @commands.command()
     async def cat(self, ctx):
         await ctx.message.edit(content="""{ \  / }
( ^ - ^ )
( u   u )～""")
     
     @commands.command()
     async def pew(self, ctx):
         """(   ' - ')>---------- pew pew"""
         await ctx.message.edit(content="(   ' - ')>---------- pew pew")
     
     @commands.command()
     async def lpew(self, ctx):
         """pew pew ----------<(' - '   )"""
         await ctx.message.edit(content="pew pew ----------<(' - '   )")
          
     
def setup(bot):
    bot.add_cog(Textemotes(bot))
