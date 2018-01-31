import discord
import asyncio
from discord.ext import commands

class Anim: 
     def __init__(self, bot):
          self.bot = bot
 
     @commands.command()
     async def dance(self, ctx):
         for i in range(1, 10, 1):
             await ctx.message.edit(content="\\\(' - '   )\\")
             await asyncio.sleep(0.7)
             await ctx.message.edit(content="/(   ' - ')/")
             await asyncio.sleep(0.7)
     
     @commands.command()
     async def virus(self, ctx, member : discord.Member = None, *, virus : str):
         wheelList = ['/', '-', '\\', '|']
         wheelIter = iter(wheelList)
         for i in range(2, 17, 2):
             try:
                 wheel = next(wheelIter)
             except StopIteration:
                 wheelIter = iter(wheelList)
                 wheel = next(wheelIter)
             await ctx.message.edit(content=f"`[{('▓' * i).ljust(16)}] {wheel} {virus}-virus.exe Packing files.`")
             await asyncio.sleep(0.6)
         await ctx.message.edit(content=f"`Injecting virus.   |`")
         await asyncio.sleep(0.9)
         await ctx.message.edit(content=f"`Injecting virus..  /`")
         await asyncio.sleep(0.9)  
         await ctx.message.edit(content=f"`Injecting virus... -`")
         await asyncio.sleep(0.9)
         await ctx.message.edit(content=f"`Successfully Injected {virus}-virus.exe into  `" + member.mention)

     async def on_message(self, message):
         for bombstr in ['=boom', '💣m']:
             if message.content.find(bombstr) != -1:
                 await self._boom(message, bombstr)
                 break

     async def _boom(self, message, toreplace):
         boomIndex = message.content.find(toreplace)
         msgBeforeBoom = message.content[:boomIndex]
         msgAfterBoom = message.content[boomIndex + len(toreplace):]
         for c in range(5, 0, -1):
             await message.edit(content= msgBeforeBoom + "`THIS MESSAGE WILL SELF DESTRUCT IN %s`" % c + msgAfterBoom)
             await asyncio.sleep(0.61)
         await message.edit(content=msgBeforeBoom + "💣" + msgAfterBoom)
         await asyncio.sleep(0.61)
         await message.edit(content=msgBeforeBoom + "💥" + msgAfterBoom)
          
     
     @commands.command()
     async def table(self, ctx):
         await ctx.message.edit(content="`(\°-°)\     ┬─┬`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(\°□°)\     ┬─┬`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(-°□°)-     ┬─┬`")
         await asyncio.sleep(0.7)
         wheelList = ['┬─┬', ']', '┻━┻', '[']
         wheelIter = iter(wheelList)
         for i in range(3, 27, 6):
             try:
                 wheel = next(wheelIter)
             except StopIteration:
                 wheelIter = iter(wheelList)
                 wheel = next(wheelIter)
             await ctx.message.edit(content=f"`(╯°□°)╯ {(i * ' ')} {wheel} `")
             await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(\°-°)\                           ┬─┬`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(\°-°)\                           ]`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(\°-°)\                                ┻━┻`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(\°-°)\                                         [`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(\°-°)\                                          ┬─┬`")
       
     @commands.command()
     async def warning(self, ctx):
         await ctx.message.edit(content="`LOAD !! WARNING !! SYSTEM OVER`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`OAD !! WARNING !! SYSTEM OVERL`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`AD !! WARNING !! SYSTEM OVERLO`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`D !! WARNING !! SYSTEM OVERLOA`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`! WARNING !! SYSTEM OVERLOAD !`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`WARNING !! SYSTEM OVERLOAD !!`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`ARNING !! SYSTEM OVERLOAD !! W`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`RNING !! SYSTEM OVERLOAD !! WA`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`NING !! SYSTEM OVERLOAD !! WAR`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`ING !! SYSTEM OVERLOAD !! WARN`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`NG !! SYSTEM OVERLOAD !! WARNI`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`G !! SYSTEM OVERLOAD !! WARNIN`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`!! SYSTEM OVERLOAD !! WARNING`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`! SYSTEM OVERLOAD !! WARNING !`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`SYSTEM OVERLOAD !! WARNING !!`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`IMMINENT SHUT-DOWN IN 0.5 SEC!`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`WARNING !! SYSTEM OVERLOAD !!`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`IMMINENT SHUT-DOWN IN 0.2 SEC!`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`SYSTEM OVERLOAD !! WARNING !!`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`IMMINENT SHUT-DOWN IN 0.01 SEC!`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`SHUT-DOWN EXIT ERROR ¯\\(｡･益･)/¯`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`CTRL + R FOR MANUAL OVERRIDE..`")
     
     @commands.command()
     async def woah(self, ctx):
         await ctx.message.edit(content="(   ' O ')")
         await asyncio.sleep(0.8)
         await ctx.message.edit(content="(  ' O ' )")
         await asyncio.sleep(0.8)
         await ctx.message.edit(content="( ' O '  )")
         await asyncio.sleep(0.8)
         await ctx.message.edit(content="(' O '   )")
         await asyncio.sleep(0.8)
         await ctx.message.edit(content="( ' O '  )")
         await asyncio.sleep(0.8)
         await ctx.message.edit(content="(  ' O ' )")
         await asyncio.sleep(0.8)
         await ctx.message.edit(content="(   ' O ')")
     
     @commands.command()
     async def deadchat(self, ctx):
         wheelList = ['DEAD CHAT', 'T DEAD CHA', 'AT DEAD CH', 'HAT DEAD C', 'CHAT DEAD', 'D CHAT DEA', 'AD CHAT DE', 'EAD CHAT D']
         wheelIter = iter(wheelList)
         for i in range(1, 10, 1):
             try:
                 wheel = next(wheelIter)
             except StopIteration:
                 wheelIter = iter(wheelList)
                 wheel = next(wheelIter)
             await ctx.message.edit(content=f"`{wheel}`")
             await asyncio.sleep(0.7)
     
     #@commands.command()
     #async def ghostie(self, ctx):
         #await ctx.message.edit(content="""(〜' - ')〜
#〜(' - '〜)""")
         #await asyncio.sleep(0.8)
         #await ctx.message.edit(content="""(〜' - ')〜
#〜(' - '〜)
     
def setup(bot):
   bot.add_cog(Anim(bot))
