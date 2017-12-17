from __future__ import division
import discord
import math
import operator
import colorthief
import asyncio
import random
import time
import datetime
import emoji
import copy
import io
import aiohttp
import json
import PIL
import os
import shutil
import requests
import urllib.parse
import urbanasync
import glob
import moviepy.editor as mpy
from discord.ext import commands
from ext.utility import parse_equation
from ext.colours import ColorNames
from urllib.request import urlopen
from bs4 import BeautifulSoup
from sympy import solve
from PIL import Image,ImageFilter,ImageDraw,ImageFont
from datetime import datetime
from discord.ext import commands
from pyparsing import (Literal,CaselessLiteral,Word,Combine,Group,Optional,
                    ZeroOrMore,Forward,nums,alphas,oneOf)
from discord.ext import commands
from ext.utility import parse_equation
from ext.colours import ColorNames
from urllib.request import urlopen
from sympy import solve
from random import randint, choice
from enum import Enum



class NumericStringParserForPython3(object):
    '''
    Most of this code comes from the fourFn.py pyparsing example

    '''
    def pushFirst(self, strg, loc, toks ):
        self.exprStack.append( toks[0] )
    def pushUMinus(self, strg, loc, toks ):
        if toks and toks[0]=='-':
            self.exprStack.append( 'unary -' )
    def __init__(self):
        """
        Please use any of the following symbols:
        expop   :: '^'
        multop  :: '*' | '/'
        addop   :: '+' | '-'
        integer :: ['+' | '-'] '0'..'9'+
        """
        point = Literal( "." )
        e     = CaselessLiteral( "E" )
        fnumber = Combine( Word( "+-"+nums, nums ) +
                        Optional( point + Optional( Word( nums ) ) ) +
                        Optional( e + Word( "+-"+nums, nums ) ) )
        ident = Word(alphas, alphas+nums+"_$")
        plus  = Literal( "+" )
        minus = Literal( "-" )
        mult  = Literal( "*" )
        div   = Literal( "/" )
        lpar  = Literal( "(" ).suppress()
        rpar  = Literal( ")" ).suppress()
        addop  = plus | minus
        multop = mult | div
        expop = Literal( "^" )
        pi    = CaselessLiteral( "PI" )
        expr = Forward()
        atom = ((Optional(oneOf("- +")) +
                (pi|e|fnumber|ident+lpar+expr+rpar).setParseAction(self.pushFirst))
                | Optional(oneOf("- +")) + Group(lpar+expr+rpar)
                ).setParseAction(self.pushUMinus)
        # by defining exponentiation as "atom [ ^ factor ]..." instead of
        # "atom [ ^ atom ]...", we get right-to-left exponents, instead of left-to-right
        # that is, 2^3^2 = 2^(3^2), not (2^3)^2.
        factor = Forward()
        factor << atom + ZeroOrMore( ( expop + factor ).setParseAction( self.pushFirst ) )
        term = factor + ZeroOrMore( ( multop + factor ).setParseAction( self.pushFirst ) )
        expr << term + ZeroOrMore( ( addop + term ).setParseAction( self.pushFirst ) )
        # addop_term = ( addop + term ).setParseAction( self.pushFirst )
        # general_term = term + ZeroOrMore( addop_term ) | OneOrMore( addop_term)
        # expr <<  general_term
        self.bnf = expr
        # this will map operator symbols to their corresponding arithmetic operations
        epsilon = 1e-12
        self.opn = {
                "+" : operator.add,
                "-" : operator.sub,
                "*" : operator.mul,
                "/" : operator.truediv,
                "^" : operator.pow }
        self.fn  = {
                "sin" : math.sin,
                "cos" : math.cos,
                "tan" : math.tan,
                "abs" : abs,
                "trunc" : lambda a: int(a),
                "round" : round,
                "sgn" : lambda a: abs(a)>epsilon and cmp(a,0) or 0}
    def evaluateStack(self, s ):
        op = s.pop()
        if op == 'unary -':
            return -self.evaluateStack( s )
        if op in "+-*/^":
            op2 = self.evaluateStack( s )
            op1 = self.evaluateStack( s )
            return self.opn[op]( op1, op2 )
        elif op == "PI":
            return math.pi # 3.1415926535
        elif op == "E":
            return math.e  # 2.718281828
        elif op in self.fn:
            return self.fn[op]( self.evaluateStack( s ) )
        elif op[0].isalpha():
            return 0
        else:
            return float( op )
    def eval(self,num_string,parseAll=True):
        self.exprStack=[]
        results=self.bnf.parseString(num_string,parseAll)
        val=self.evaluateStack( self.exprStack[:] )
        return val

class Misc:
    def __init__(self, bot):
        self.bot = bot
        self.emoji_converter = commands.EmojiConverter()
        self.nsp=NumericStringParserForPython3()

    @commands.command()
    async def embedtext(self, ctx, *, message):
        '''embed messages '''
        await ctx.message.delete()
        em = discord.Embed(color=random.randint(0, 0xFFFFFF))
        em.description = message
        await ctx.send(embed=em)

    @commands.command()
    async def react(self, ctx, index: int, *, reactions):
        '''React to a specified message with reactions'''
        history = await ctx.channel.history(limit=10).flatten()
        message = history[index]
        async for emoji in self.validate_emojis(ctx, reactions):
            await message.add_reaction(emoji)

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
        emb.color = await ctx.get_dominant_color(url=ctx.message.author.avatar_url)
        definition = term.definitions[definition_number]
        emb.title = f"{definition.word}  ({definition_number+1}/{len(term.definitions)})"
        emb.description = definition.definition
        emb.url = definition.permalink
        emb.add_field(name='Example', value=definition.example)
        emb.add_field(name='Votes', value=f'{definition.upvotes}👍    {definition.downvotes}👎')
        emb.set_footer(text=f"Definition written by {definition.author}", icon_url="http://urbandictionary.com/favicon.ico")
        await ctx.send(embed=emb)

    @commands.group(invoke_without_command=True)
    async def lenny(self, ctx):
        """group commands"""
        msg = 'Available: `{}lenny face`, `{}lenny shrug`, `{}lenny tableflip`, `{}lenny unflip`'
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
        """Unfips!"""
        await ctx.message.edit(content='┬─┬﻿ ノ( ゜-゜ノ)')

    @lenny.command()
    async def face(self, ctx):
        """Lenny Face!"""
        await ctx.message.edit(content='( ͡° ͜ʖ ͡°)')

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
