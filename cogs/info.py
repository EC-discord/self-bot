import discord
from discord.ext import commands
from urllib.parse import urlparse
from ext import embedtobox
import datetime
import asyncio
import psutil
import random
import pip
import os
import io


class Information:
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(aliases=['bot', 'info'])
    async def selfinfo(self, ctx):
        '''See information about the bot'''
        embed = discord.Embed()
        embed.colour = await ctx.get_dominant_color(ctx.author.avatar_url)
        embed.set_author(name='BOT', icon_url=ctx.author.avatar_url)

        total_members = sum(1 for _ in self.bot.get_all_members())
        total_online = len({m.id for m in self.bot.get_all_members() if m.status is discord.Status.online})
        total_unique = len(self.bot.users)

        voice_channels = []
        text_channels = []
        for guild in self.bot.guilds:
            voice_channels.extend(guild.voice_channels)
            text_channels.extend(guild.text_channels)

        text = len(text_channels)
        voice = len(voice_channels)
        dm = len(self.bot.private_channels)

        now = datetime.datetime.utcnow()
        delta = now - self.bot.uptime
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        fmt = '{h}h {m}m {s}s'
        if days:
            fmt = '{d}d ' + fmt
        uptime = fmt.format(d=days, h=hours, m=minutes, s=seconds)
        embed.add_field(name='Author', value='QoS (N)')
        embed.add_field(name='Uptime', value=uptime)
        embed.add_field(name='Guilds', value=len(self.bot.guilds))
        embed.add_field(name='Members', value=f'{total_unique} total\n{total_online} online')
        embed.add_field(name='Channels', value=f'{text} text\n{voice} voice\n{dm} direct')
        embed.set_footer(text=f'DiscordSelfbot derived ,js')
        await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Information(bot))
