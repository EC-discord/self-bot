import discord
import asyncio
from discord.ext import commands

class Textemotes(commands.Cog): 
     def __init__(self, bot):
          self.bot = bot
          
     @commands.command()
     async def snipe(self, ctx, member : discord.Member = None):
          member = member or None
          if member is None:
               await ctx.message.edit(content = '(　-_･) ︻デ═一"    ▸')
          else:
              await ctx.message.edit(content = f'(　-_･) ︻デ═一"    ▸ {member.mention}')
    
     @commands.command()
     async def powa(self, ctx):
         """(づ｡◕‿‿◕｡)づ"""
         await ctx.message.edit(content="(づ｡◕‿‿◕｡)づ")
     
     @commands.command()
     async def flip(self, ctx):
         """(づ｡◕‿‿◕｡)づ︵ ┻━┻"""
         await ctx.message.edit(content="(づ｡◕‿‿◕｡)づ︵ ┻━┻")
     
     @commands.command()
     async def thumbs(self, ctx):
         """(👍' - ')👍"""
         await ctx.message.edit(content="(👍' - ')👍")
    
     @commands.command(aliases = ["bye"])
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
     async def cookie(self, ctx):
         """(  ^ - ^)-🍪"""
         await ctx.message.edit(content="(  ^ - ^)-🍪")
          
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

     @commands.command()
     async def dawae(self, ctx):
         """shows you DA WAE"""
         await ctx.message.edit(content=""".....::::::･''･::::::.... ..... 
:::::･'''　　　　　'''･:::::
::　　　　　　　　　::
:　　  DA WAE   　         :
::　　　　　　　　　::
::･...　　　　　　...･::
　　'''::::::･,,･::::::'''
　     　∩∧_∧∩
　　　(　･ω･)
　　 　/　　ﾉ
　　　しーU""")                               
     
     @commands.command()
     async def life(self, ctx):
          """get a life"""
          await ctx.message.edit(content = """ຸ               ∧ ＿ ∧
　        ( ・ω・) 
┏━Ｕ━━━Ｕ━┓
┃　  Get A Life      ┃
┗━━━━━━━┛""")
                                
     
     
     
def setup(bot):
    bot.add_cog(Textemotes(bot))
