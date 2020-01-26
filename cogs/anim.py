import discord
import asyncio
from discord.ext import commands

class anim(commands.Cog):
     """animated messages"""
     def __init__(self, bot):
          self.bot = bot
     @commands.command()
     async def cathi(self, ctx, text: str = "Hi..."):
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
         for i in range(2):
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
          await ctx.message.edit(content = "(   ° - °) (' - '   )")
          await asyncio.sleep(1)
          await ctx.message.edit(content = "(\\\° - °)\ (' - '   )")
          await asyncio.sleep(1)
          await ctx.message.edit(content = "(—°□°)— (' - '   )")
          await asyncio.sleep(1)
          await ctx.message.edit(content = "(╯°□°)╯(' - '   )")
          await asyncio.sleep(1)
          await ctx.message.edit(content = "(╯°□°)╯︵(\\\ .o.)\\")

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
         for counter in range(5, -1, -1):
             await ctx.message.edit(content = f"`THIS MESSAGE WILL SELF DESTRUCT IN {counter}`")
             await asyncio.sleep(1)
         await ctx.message.edit(content = "💣")
         await asyncio.sleep(1)
         await ctx.message.edit(content = "💥")
          
     
     @commands.command()
     async def table(self, ctx):
         t = (']', '┻━┻', '[',  '┬─┬')
         await ctx.message.edit(content=f"`(\°-°)\ {t[4]}`")
         await asyncio.sleep(1)
         await ctx.message.edit(content=f"`(\°□°)\ {t[4]}`")
         await asyncio.sleep(1)
         await ctx.message.edit(content=f"`(-°□°)- {t[4]}`")
         await asyncio.sleep(1)
         await ctx.message.edit(content=f"`(╯°□°)╯ {t[1]}`")
         await asyncio.sleep(1)
         await ctx.message.edit(content=f"`(╯°□°)╯  {t[2]}`")                                    
         await asyncio.sleep(1)
         await ctx.message.edit(content=f"`(╯°□°)╯   {t[3]}`")
         await asyncio.sleep(1)
         await ctx.message.edit(content=f"`(╯°□°)╯    {t[4]}`")                           
         await asyncio.sleep(1)
         await ctx.message.edit(content=f"`(╯°□°)╯     {t[1]}`")                           
         await asyncio.sleep(1)
         await ctx.message.edit(content=f"`(╯°□°)╯      {t[2]}`")                           
         await asyncio.sleep(1)
         await ctx.message.edit(content=f"`(╯°□°)╯       {t[3]}`")                           
         await asyncio.sleep(1)                                    
         await ctx.message.edit(content=f"`(\°-°)\        {t[4]}`")                           
       
     @commands.command()
     async def warning(self, ctx):
         await ctx.message.edit(content="`LOAD !! WARNING !! SYSTEM OVER`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`OAD !! WARNING !! SYSTEM OVERL`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`AD !! WARNING !! SYSTEM OVERLO`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`D !! WARNING !! SYSTEM OVERLOA`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`! WARNING !! SYSTEM OVERLOAD !`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`WARNING !! SYSTEM OVERLOAD !!`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`ARNING !! SYSTEM OVERLOAD !! W`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`RNING !! SYSTEM OVERLOAD !! WA`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`NING !! SYSTEM OVERLOAD !! WAR`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`ING !! SYSTEM OVERLOAD !! WARN`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`NG !! SYSTEM OVERLOAD !! WARNI`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`G !! SYSTEM OVERLOAD !! WARNIN`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`!! SYSTEM OVERLOAD !! WARNING`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`! SYSTEM OVERLOAD !! WARNING !`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`SYSTEM OVERLOAD !! WARNING !!`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`IMMINENT SHUT-DOWN IN 0.5 SEC!`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`WARNING !! SYSTEM OVERLOAD !!`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`IMMINENT SHUT-DOWN IN 0.2 SEC!`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`SYSTEM OVERLOAD !! WARNING !!`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`IMMINENT SHUT-DOWN IN 0.01 SEC!`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`SHUT-DOWN EXIT ERROR ¯\\(｡･益･)/¯`")
         await asyncio.sleep(1)
         await ctx.message.edit(content="`CTRL + R FOR MANUAL OVERRIDE..`")
     
     @commands.command()
     async def deadchat(self, ctx):
         dead = ('DEAD CHAT', 'T DEAD CHA', 'AT DEAD CH', 'HAT DEAD C', 'CHAT DEAD', 'D CHAT DEA', 'AD CHAT DE', 'EAD CHAT D', 'DEAD CHAT')
         for d in dead:
             await ctx.message.edit(content=d)
             await asyncio.sleep(1)
                                    
def setup(bot):
   bot.add_cog(anim(bot))
