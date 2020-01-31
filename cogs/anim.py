import discord
import asyncio
from discord.ext import commands

class anim(commands.Cog):
     """animated messages"""
     def __init__(self, bot):
          self.bot = bot
     @commands.command()
     async def cathi(self, ctx, *, text: str = None):
         if text == None:
             text = "Hi..."
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
                await ctx.message.edit(content=cat)
                await asyncio.sleep(1.5)
                   
     @commands.command()
     async def loading(self, ctx):
         for num in range(1, 6, 1):
             dots = "." * num
             spaces = " " * (abs(num - 5))
             await ctx.message.edit(content = f"```loading.{dots}{spaces}{num}%```")
             await asyncio.sleep(1)
         await ctx.message.edit(content = "``` Error! :C```")
         await asyncio.sleep(1)
         await ctx.message.edit(content = "```Reloading......```")    
          
     @commands.command()
     async def flop(self, ctx):
         list = ("(   ° - °) (' - '   )",
                 "(\\\° - °)\ (' - '   )",
                 "(—°□°)— (' - '   )",
                 "(╯°□°)╯(' - '   )",
                 "(╯°□°)╯︵(\\\ .o.)\\")
         for i in list:
             await ctx.message.edit(content = i)
             await asyncio.sleep(1.5)
     @commands.command()
     async def poof(self, ctx):
         """poofness"""
         await ctx.message.edit(content = "(   ' - ')")
         await asyncio.sleep(1)
         await ctx.message.edit(content = "' - ')")
         await asyncio.sleep(1)
         await ctx.message.edit(content = "- ')")
         await asyncio.sleep(1)
         await ctx.message.edit(content = "')")
         await asyncio.sleep(1)
         await ctx.message.edit(content = ")")
         await asyncio.sleep(1)
         await ctx.message.edit(content = "*poofness*")
     
     @commands.command()
     async def virus(self, ctx, member: discord.Member = None, *, virus: str = "trojan"):
         wheelList = ['/', '-', '\\', '|']
         wheelIter = iter(wheelList)
         for i in range(2, 17, 2):
             try:
                 wheel = next(wheelIter)
             except StopIteration:
                 wheelIter = iter(wheelList)
                 wheel = next(wheelIter)
             await ctx.message.edit(content=f"`[{('▓' * i).ljust(16)}] {wheel} {virus}-virus.exe Packing files.`")
             await asyncio.sleep(1)
         await ctx.message.edit(content=f"`Injecting virus.   |`")
         await asyncio.sleep(1)
         await ctx.message.edit(content=f"`Injecting virus..  /`")
         await asyncio.sleep(1)  
         await ctx.message.edit(content=f"`Injecting virus... -`")
         await asyncio.sleep(1)
         await ctx.message.edit(content=f"`Successfully Injected {virus}-virus.exe into {member.name}`")

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
             await ctx.message.edit(content=d)
                                    
def setup(bot):
   bot.add_cog(anim(bot))
