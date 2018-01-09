import discord
import asyncio
from discord.ext import commands

class Anim: 
     def __init__(self, bot):
          self.bot = bot

     @commands.command()
     async def boom(self, ctx):
         for c in range(5, 0, -1):
            await ctx.message.edit(content="`THIS MESSAGE WILL SELF DESTRUCT IN %s`" % c)
            await asyncio.sleep(0.6)
         await ctx.message.edit(content="💣")
         await asyncio.sleep(0.6)
         await ctx.message.edit(content="💥")
     
     @commands.command
     async def hax(self, ctx):
         print ('be ye here the see dis command executesu')
         msg = await ctx.send(content="`[▓▓▓                    ] / {virus}-virus.exe Packing files.`")
         await asyncio.sleep(0.4)
         await ctx.message.edit(content="`[▓▓▓▓▓▓▓                ] - {virus}-virus.exe Packing files..`")
         await asyncio.sleep(0.4)
         await ctx.message.edit(content="`[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {virus}-virus.exe Packing files..`")
         await asyncio.sleep(0.4)
         await ctx.message.edit(content="`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}-virus.exe Packing files..`")
         await asyncio.sleep(0.4)
         await ctx.message.edit(content="`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}-virus.exe Packing files..`")
         await asyncio.sleep(0.4)
         await ctx.message.edit(content="`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}-virus.exe Packing files..`")
         await asyncio.sleep(0.4)
         await ctx.message,edit(content="`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}-virus.exe Packing files..`")
         await asyncio.sleep(0.4)
         await ctx.message.edit(content="`Successfully downloaded {virus}-virus.exe`")
         await asyncio.sleep(0.4)
         await ctx.message.edit(content="`Injecting virus.   |`")
         await asyncio.sleep(0.4)
         await ctx.message.edit(content="`Injecting virus..  /`")
         await asyncio.sleep(0.4)
         await ctx.message.edit(content="`Injecting virus... -`")
         await asyncio.sleep(0.4)
         await ctx.message.edit(content="`Successfully Injected {virus}-virus.exe into {user}`")
       
def setup(bot):
   bot.add_cog(Anim(bot))
