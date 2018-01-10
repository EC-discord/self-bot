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
            await asyncio.sleep(0.61)
         await ctx.message.edit(content="💣")
         await asyncio.sleep(0.61)
         await ctx.message.edit(content="💥")
     
     @commands.command()
     async def virus(self, ctx,*, args):
         await ctx.message.send(content="`[▓▓▓                    ] / {virus}.exe Packing files.`")
         await asyncio.sleep(0.4)
         await ctx.message.edit(content="`[▓▓▓▓▓▓▓                ] - {virus}.exe Packing files..`")
         await asyncio.sleep(0.4)
         await ctx.message.edit(content="`[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {virus}.exe Packing files..`")
         await asyncio.sleep(0.4)
         await ctx.message.edit(content="`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}.exe Packing files..`")
         await asyncio.sleep(0.4)
         await ctx.message.edit(content="`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}.exe Packing files..`")
         await asyncio.sleep(0.4)
         await ctx.message.edit(content="`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}.exe Packing files..`")
         await asyncio.sleep(0.4)
         await ctx.message.edit(content="`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}.exe Packing files..`")
         await asyncio.sleep(0.4)
         await ctx.message.edit(content="`Successfully downloaded {virus}.exe`")
         await asyncio.sleep(0.6)
         await ctx.message.edit(content="`Injecting virus.   |`")
         await asyncio.sleep(0.6)
         await ctx.message.edit(content="`Injecting virus..  /`")
         await asyncio.sleep(0.6)
         await ctx.message.edit(content="`Injecting virus... -`")
         await asyncio.sleep(0.6)
         await ctx.message.author(content="{1} successfully Injected {virus}.exe into  {0.mention}".format(args, ctx.message.author) )
       
def setup(bot):
   bot.add_cog(Anim(bot))
