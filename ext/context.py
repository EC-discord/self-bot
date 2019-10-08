import discord
from discord.ext import commands
import asyncio
from colorthief import ColorThief
from urllib.parse import urlparse
import io
import os

class CustomContext(commands.Context):
    '''Custom Context class to provide utility.'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def session(self):
        '''Returns the bot's aiohttp client session'''
        return self.bot.session

    def delete(self):
        '''shortcut'''
        return self.message.delete()

    async def get_ban(self, name_or_id):
        '''Helper function to retrieve a banned user'''
        for ban in await self.guild.bans():
            if name_or_id.isdigit():
                if ban.user.id == int(name_or_id):
                    return ban
            if name_or_id.lower() in str(ban.user).lower():
                return ban

    async def purge(self, *args, **kwargs):
        '''Shortcut to channel.purge, preset for selfbots.'''
        kwargs.setdefault('bulk', False)
        await self.channel.purge(*args, **kwargs)

    async def get_dominant_color(self, url=None, quality=10):
        '''Returns the dominant color of an image from a url'''
        maybe_col = os.environ.get('COLOR')

        url = url or self.author.avatar_url

        if maybe_col:
            raw = int(maybe_col.strip('#'), 16)
            return discord.Color(value=raw)
        try:
            async with self.session.get(url) as resp:
                image = await resp.read()
        except:
            return discord.Color.default()

        with io.BytesIO(image) as f:
            try:
                color = ColorThief(f).get_color(quality=quality)
            except:
                return discord.Color.dark_grey()
            
        return discord.Color.from_rgb(*color)

    async def success(self, msg=None, delete=False):
        if delete:
            await ctx.message.delete()
        if msg:
            await self.send(msg)
        else:
            await self.message.add_reaction('✔')

    async def failure(self, msg=None):
        if msg:
            await self.send(msg)
        else:
            await self.message.add_reaction('❌')

    @staticmethod
    def paginate(text: str):
        '''Simple generator that paginates text.'''
        last = 0
        pages = []
        for curr in range(0, len(text)):
            if curr % 1980 == 0:
                pages.append(text[last:curr])
                last = curr
                appd_index = curr
        if appd_index != len(text)-1:
            pages.append(text[last:curr])
        return list(filter(lambda a: a != '', pages))
