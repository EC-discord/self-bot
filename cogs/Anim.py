import discord
import asyncio
from discord.ext import commands

class Anim: 
     def __init__(self, bot):
          self.bot = bot
     
     
     async def on_message(self, message):
         if message.content.find('=boom') != -1:
             await self._boom(message) 
         elif message.content('=boom'):
             for c in range(5, 0, -1):
                 await message.edit(content="THIS MESSAGE WILL SELF DESTRUCT IN %s" % c)
                 await asyncio.sleep(0.61)
             await message.edit(content="💣")
             await asyncio.sleep(0.61)
             await message.edit(content="💥")
             
          
     async def _boom(self, message):
         boomIndex = message.content.find('=boom')
         msgBeforeBoom = message.content[:boomIndex]
         msgAfterBoom = message.content[boomIndex + len('boom'):]
         for c in range(5, 0, -1):
             await message.edit(content= msgBeforeBoom + "`THIS MESSAGE WILL SELF DESTRUCT IN %s`" % c + msgAfterBoom)
             await asyncio.sleep(0.61)
         await message.edit(content=msgBeforeBoom + "💣" + msgAfterBoom)
         await asyncio.sleep(0.61)
         await message.edit(content=msgBeforeBoom + "💥" + msgAfterBoom)
             
     @commands.command()
     async def animpres(self, ctx):
         while True:
             for c in range(5, 0, -1):
                 await ctx.send("=presence online (\°□°)\  ┬─┬")
                 await asyncio.sleep(2.7)
                 await ctx.send("=presence online (-°□°)-  ┬─┬")
                 await asyncio.sleep(2.7)
                 await ctx.send("=presence online (╯°□°)╯    ]")
                 await asyncio.sleep(2.7)
                 await ctx.send("=presence online (╯°□°)╯     ┻━┻")
                 await asyncio.sleep(13)
     
     @commands.command()
     async def virus(self, ctx):
         await ctx.message.edit(content="`[▓▓▓                    ] / {virus}.exe Packing files.`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`[▓▓▓▓▓▓▓                ] - {virus}.exe Packing files..`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {virus}.exe Packing files..`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}.exe Packing files..`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}.exe Packing files..`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}.exe Packing files..`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}.exe Packing files..`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`Successfully downloaded {virus}.exe`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`Injecting virus.   |`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`Injecting virus..  /`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`Injecting virus... -`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`Successfully Injected {virus}.exe into User`")
     
     @commands.command()
     async def table(self, ctx):
         await ctx.message.edit(content="`(\°-°)\  ┬─┬`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(\°□°)\  ┬─┬`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(-°□°)-  ┬─┬`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(╯°□°)╯    ]`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(╯°□°)╯     ┻━┻`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(╯°□°)╯       [`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(╯°□°)╯          ┬─┬`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(╯°□°)╯                 ]`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(╯°□°)╯                  ┻━┻`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(╯°□°)╯                         [`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(\°-°)\                               ┬─┬`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(\°-°)\                                     ]`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(\°-°)\                                       ┻━┻`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(\°-°)\                                               [`")
         await asyncio.sleep(0.7)
         await ctx.message.edit(content="`(\°-°)\                                              ┬─┬`")
       
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
         await asyncio.sleep(1)
         await ctx.message.edit(content="(' O '   )")
         await asyncio.sleep(1)
         await ctx.message.edit(content="(  ' O '  )")
         await asyncio.sleep(1)
         await ctx.message.edit(content="(  . O .  )")
     
     #@commands.command()
     #async def ghostie(self, ctx):
         #await ctx.message.edit(content="""(〜' - ')〜
#〜(' - '〜)""")
         #await asyncio.sleep(0.8)
         #await ctx.message.edit(content="""(〜' - ')〜
#〜(' - '〜)
     
def setup(bot):
   bot.add_cog(Anim(bot))
