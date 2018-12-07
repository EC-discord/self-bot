from __future__ import division
import discord
import asyncio
import random
import time
import datetime
import emoji
import json
import requests
import urllib.parse
import urbanasync
from discord.ext import commands
from ext.utility import parse_equation
from ext.colours import ColorNames
from urllib.request import urlopen
from bs4 import BeautifulSoup
from PIL import Image,ImageFilter,ImageDraw,ImageFont
from datetime import datetime
from discord.ext import commands
from pyparsing import (Literal,CaselessLiteral,Word,Combine,Group,Optional,
                    ZeroOrMore,Forward,nums,alphas,oneOf)
from discord.ext import commands
from ext.utility import parse_equation
from ext.colours import ColorNames
from urllib.request import urlopen
import io
from random import randint, choice    


class Misc:
    def __init__(self, bot):
        self.bot = bot
        self.emoji_converter = commands.EmojiConverter()
        self.emoji_list = []
        
    @commands.command()
    async def hexcode(self, ctx, *, role):
      """the role argument can be the name of the role or its tag"""
      if isinstance(role, discord.Role):
        await ctx.send(role.color)
      else:
        role = discord.utils.get(ctx.guild.roles, name = role)
        await ctx.send(role.color)

    @commands.command()
    async def embedtext(self, ctx, *, message):
        '''embed messages '''
        await ctx.message.delete()
        em = discord.Embed(color=random.randint(0, 0xFFFFFF))
        em.description = message
        await ctx.send(embed=em)
    
    @commands.command(aliases = ["rr"])
    async def randomreact(self, ctx, messageNo: int, no_of_reactions : int = 20):
        '''React to a message with random custom emojis'''
        self.emoji_list = []
        messageid = 0
        await ctx.message.delete()
        for emoji in self.bot.emojis:
          if emoji.name.startswith("GW"):
            self.emoji_list.append(emoji)
        async for message in ctx.channel.history(limit = 25):  
          if messageid != messageNo:
            messageid += 1
            continue
          for i in range(no_of_reactions):
            emoji = random.choice(self.emoji_list)
            await message.add_reaction(emoji)
            self.emoji_list.remove(emoji)
          break

    @commands.command()
    async def react(self, ctx, index: int, *, reactions):
        '''React to a specified message with reactions'''
        history = await ctx.channel.history(limit=30).flatten()
        message = history[index]
        async for emoji in self.validate_emojis(ctx, reactions):
            await message.add_reaction(emoji)
        await ctx.message.delete()

    async def validate_emojis(self, ctx, reactions):
        '''
        Checks if an emoji is valid otherwise,
        tries to convert it into a custom emoji
        '''
        for emote in reactions.split():
            if emote in emoji.UNICODE_EMOJI:
                yield emote
            else:
                try:
                    yield await self.emoji_converter.convert(ctx, emote)
                except commands.BadArgument:
                    pass

    @commands.command(aliases=['color', 'colour', 'sc'])
    async def get_color(self, ctx, *, color: discord.Colour):
        '''Enter a color and you will see it!'''
        file = io.BytesIO()
        Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
        file.seek(0)
        em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
        em.set_image(url='attachment://color.png')
        await ctx.send(file=discord.File(file, 'color.png'), embed=em)

    def check_emojis(self, bot_emojis, emoji):
        for exist_emoji in bot_emojis:
            if emoji[0] == "<" or emoji[0] == "":
                if exist_emoji.name.lower() == emoji[1]:
                    return [True, exist_emoji]
            else:
                if exist_emoji.name.lower() == emoji[0]:
                    return [True, exist_emoji]
        return [False, None]

    @commands.group(invoke_without_command=True, name='emoji', aliases=['emote', 'e'])
    async def _emoji(self, ctx, *, emoji: str):
        '''send emoji pic'''
        emoji = emoji.split(":")
        emoji_check = self.check_emojis(ctx.bot.emojis, emoji)
        if emoji_check[0]:
            emo = emoji_check[1]
        else:
            emoji = [e.lower() for e in emoji]
            if emoji[0] == "<" or emoji[0] == "":
                emo = discord.utils.find(lambda e: emoji[1] in e.name.lower(), ctx.bot.emojis)
            else:
                emo = discord.utils.find(lambda e: emoji[0] in e.name.lower(), ctx.bot.emojis)
            if emo == None:
                em = discord.Embed(title="None", description="No emoji found.")
                em.color = await ctx.get_dominant_color(ctx.author.avatar_url)
                await ctx.send(embed=em)
                return
        async with ctx.session.get(emo.url) as resp:
            image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.message.delete()
            await ctx.send(file=discord.File(file, 'emote.png'))

    @commands.command()
    async def urban(self, ctx, *, search_terms: str):
        '''Urban Dictionary'''
        client = urbanasync.Client(ctx.session)
        search_terms = search_terms.split()
        definition_number = terms = None
        try:
            definition_number = int(search_terms[-1]) - 1
            search_terms.remove(search_terms[-1])
        except ValueError:
            definition_number = 0
        if definition_number not in range(0, 11):
            pos = 0
        search_terms = " ".join(search_terms)
        emb = discord.Embed()
        try:
            term = await client.get_term(search_terms)
        except LookupError:
            emb.title = "Search term not found."
            return await ctx.send(embed=emb)
        emb.color = await ctx.get_dominant_color(url=ctx.message.author.avatar_url_as(static_format = "png"))
        definition = term.definitions[definition_number]
        emb.title = f"{definition.word}  ({definition_number+1}/{len(term.definitions)})"
        emb.description = definition.definition
        emb.url = definition.permalink
        emb.add_field(name='Example', value=definition.example)
        emb.add_field(name='Votes', value=f'{definition.upvotes}👍    {definition.downvotes}👎')
        emb.set_footer(text=f"Definition written by {definition.author}", icon_url="http://urbandictionary.com/favicon.ico")
        await ctx.send(embed=emb)

    @commands.command()
    async def textemote(self, ctx, *, msg):
        """Convert text into emojis"""
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            pass

        if msg != None:
            out = msg.lower()
            text = out.replace(' ', '    ').replace('10', '\u200B:keycap_ten:')\
                      .replace('ab', '\u200B🆎').replace('cl', '\u200B🆑')\
                      .replace('0', '\u200B:zero:').replace('1', '\u200B:one:')\
                      .replace('2', '\u200B:two:').replace('3', '\u200B:three:')\
                      .replace('4', '\u200B:four:').replace('5', '\u200B:five:')\
                      .replace('6', '\u200B:six:').replace('7', '\u200B:seven:')\
                      .replace('8', '\u200B:eight:').replace('9', '\u200B:nine:')\
                      .replace('!', '\u200B❗').replace('?', '\u200B❓')\
                      .replace('vs', '\u200B🆚').replace('.', '\u200B🔸')\
                      .replace(',', '🔻').replace('a', '\u200B🅰')\
                      .replace('b', '\u200B🅱').replace('c', '\u200B🇨')\
                      .replace('d', '\u200B🇩').replace('e', '\u200B🇪')\
                      .replace('f', '\u200B🇫').replace('g', '\u200B🇬')\
                      .replace('h', '\u200B🇭').replace('i', '\u200B🇮')\
                      .replace('j', '\u200B🇯').replace('k', '\u200B🇰')\
                      .replace('l', '\u200B🇱').replace('m', '\u200B🇲')\
                      .replace('n', '\u200B🇳').replace('ñ', '\u200B🇳')\
                      .replace('o', '\u200B🅾').replace('p', '\u200B🅿')\
                      .replace('q', '\u200B🇶').replace('r', '\u200B🇷')\
                      .replace('s', '\u200B🇸').replace('t', '\u200B🇹')\
                      .replace('u', '\u200B🇺').replace('v', '\u200B🇻')\
                      .replace('w', '\u200B🇼').replace('x', '\u200B🇽')\
                      .replace('y', '\u200B🇾').replace('z', '\u200B🇿')
            try:
                await ctx.send(text)
            except Exception as e:
                await ctx.send(f'```{e}```')
        else:
            await ctx.send('Args req!', delete_after=3.0)



def setup(bot):
    bot.add_cog(Misc(bot))
