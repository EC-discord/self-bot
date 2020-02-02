import discord
import asyncio
from discord.ext import commands

class anim(commands.Cog):
     """animated messages"""
     def __init__(self, bot):
          self.bot = bot
     @commands.command()
     async def cathi(self, ctx, *, text: str = "Hi..."):
         list = ("""ຸ 　　　＿＿_＿＿
　　／　／　  ／|"
　　|￣￣￣￣|　|
　　|　　　　|／
　　￣￣￣￣""", f"""ຸ 　　　{text}
 　   　 ∧＿∧＿_
　　／(´･ω･`)  ／＼
　／|￣￣￣￣|＼／
　　|　　　　|／
　　￣￣￣￣""")
         for i in range(3):
             for cat in list:
               await asyncio.sleep(1.5)
               await ctx.message.edit(content=cat)                   
          
     @commands.command()
     async def flop(self, ctx):
         list = ("(   ° - °) (' - '   )",
                 "(\\\° - °)\ (' - '   )",
                 "(—°□°)— (' - '   )",
                 "(╯°□°)╯(' - '   )",
                 "(╯°□°)╯︵(\\\ .o.)\\")
         for i in list:
             await asyncio.sleep(1.5)
             await ctx.message.edit(content = i)
               
     @commands.command()
     async def poof(self, ctx):
         """poofness"""
         list = ("(   ' - ')",
                 "' - ')",
                 "- ')",
                 "')",
                 ")",
                 "*poofness*")
         for i in list:
             await asyncio.sleep(1.5)
             await ctx.message.edit(content=i)
     
     @commands.command()
     async def virus(self, ctx, user: discord.Member = None, *, virus: str = "trojan"):
         list = (f"``[▓▓▓                    ] / {virus}-virus.exe Packing files.``",
                 f"``[▓▓▓▓▓▓▓                ] - {virus}-virus.exe Packing files..``",
                 f"``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {virus}-virus.exe Packing files..``",
                 f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}-virus.exe Packing files..``",
                 f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}-virus.exe Packing files..``",
                 f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}-virus.exe Packing files..``",
                 f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}-virus.exe Packing files..``",
                 f"``Successfully downloaded {virus}-virus.exe``",
                 "``Injecting virus.   |``",
                 "``Injecting virus..  /``",
                 "``Injecting virus... -``",
                 f"``Successfully Injected {virus}-virus.exe into {user.name}``")
         for i in list:
             await acyncio.sleep(1.5)
             await ctx.message.edit(content=i)

     @commands.command()
     async def boom(self, ctx):
         list = ("```THIS MESSAGE WILL SELFDESTRUCT IN 5```",
                 "```THIS MESSAGE WILL SELFDESTRUCT IN 4```",
                 "```THIS MESSAGE WILL SELFDESTRUCT IN 3```",
                 "```THIS MESSAGE WILL SELFDESTRUCT IN 2```",
                 "```THIS MESSAGE WILL SELFDESTRUCT IN 1```",
                 "```THIS MESSAGE WILL SELFDESTRUCT IN 0```",
                 "💣",
                 "💥")
         for i in list:
             await asyncio.sleep(1.5)
             await ctx.message.edit(content=i)               
          
     
     @commands.command()
     async def table(self, ctx):
         list = ("`(\°-°)\  ┬─┬`",
                 "`(\°□°)\  ┬─┬`",
                 "`(-°□°)-  ┬─┬`",
                 "`(╯°□°)╯    ]`",
                 "`(╯°□°)╯     ┻━┻`",
                 "`(╯°□°)╯       [`",
                 "`(╯°□°)╯          ┬─┬`",
                 "`(╯°□°)╯                 ]`",
                 "`(╯°□°)╯                  ┻━┻`",
                 "`(╯°□°)╯                         [`",
                 "`(\°-°)\                               ┬─┬`")
         for i in list:
             await asyncio.sleep(1.5)
             await ctx.message.edit(content=i)                    
       
     @commands.command()
     async def warning(self, ctx):
         list = ("`LOAD !! WARNING !! SYSTEM OVER`",
                 "`OAD !! WARNING !! SYSTEM OVERL`",
                 "`AD !! WARNING !! SYSTEM OVERLO`",
                 "`D !! WARNING !! SYSTEM OVERLOA`",
                 "`! WARNING !! SYSTEM OVERLOAD !`",
                 "`WARNING !! SYSTEM OVERLOAD !!`",
                 "`ARNING !! SYSTEM OVERLOAD !! W`",
                 "`RNING !! SYSTEM OVERLOAD !! WA`",
                 "`NING !! SYSTEM OVERLOAD !! WAR`",
                 "`ING !! SYSTEM OVERLOAD !! WARN`",
                 "`NG !! SYSTEM OVERLOAD !! WARNI`",
                 "`G !! SYSTEM OVERLOAD !! WARNIN`",
                 "`!! SYSTEM OVERLOAD !! WARNING`",
                 "`! SYSTEM OVERLOAD !! WARNING !`",
                 "`SYSTEM OVERLOAD !! WARNING !!`",
                 "`IMMINENT SHUT-DOWN IN 0.5 SEC!`",
                 "`WARNING !! SYSTEM OVERLOAD !!`",
                 "`IMMINENT SHUT-DOWN IN 0.2 SEC!`",
                 "`SYSTEM OVERLOAD !! WARNING !!`",
                 "`IMMINENT SHUT-DOWN IN 0.01 SEC!`",                                    
                 "`SHUT-DOWN EXIT ERROR ¯\\(｡･益･)/¯",
                 "`CTRL + R FOR MANUAL OVERRIDE..`")
         for i in list:
             await asyncio.sleep(1.5)               
             await ctx.message.edit(content=i)
     
     @commands.command()
     async def deadchat(self, ctx):
         list = ('DEAD CHAT',
                 'T DEAD CHA',
                 'AT DEAD CH',
                 'HAT DEAD C',
                 'CHAT DEAD',
                 'D CHAT DEA',
                 'AD CHAT DE',
                 'EAD CHAT D',
                 'DEAD CHAT')
         for i in list:
             await asyncio.sleep(1.5)                       
             await ctx.message.edit(content=i)
                                    
def setup(bot):
   bot.add_cog(anim(bot))
