import discord
import asyncio
from discord.ext import commands

class EC: 
     def __init__(self, bot):
          self.bot = bot


    @commands.group(invoke_without_command=True)
    async def lenny(self, ctx):
        """group commands"""
        msg = 'Available: `{}lenny face`, `{}lenny shrug`, `{}lenny flip`, `{}unflip`, `{}lenny gib`'
        await ctx.send(msg.format(ctx.prefix))

    @lenny.command()
    async def shrug(self, ctx):
        """Shrugs!"""
        await ctx.message.edit(content='¯\\\_(ツ)\_/¯')

    @lenny.command()
    async def tableflip(self, ctx):
        """Tableflip!"""
        await ctx.message.edit(content='(╯°□°）╯︵ ┻━┻')

    @lenny.command()
    async def unflip(self, ctx):
        """Unflips!"""
        await ctx.message.edit(content='┬─┬﻿ ノ( ゜-゜ノ)')

    @lenny.command()
    async def lenny(self, ctx):
        """Lenny Face!"""
        await ctx.message.edit(content='( ͡° ͜ʖ ͡°)')
    
    @lenny.command()
    async def gib(self, ctx):
        await crx.message.edit(content='(づ｡◕‿‿◕｡)づ')
    
def setup(bot):
    bot.add_cog(EC(bot))
