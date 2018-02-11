import discord
from discord.ext import commands
from discord.ext.commands import TextChannelConverter
from contextlib import redirect_stdout
from ext.utility import load_json
from urllib.parse import quote as uriquote
from lxml import etree
from ext import fuzzy
from ext import embedtobox
from PIL import Image
import unicodedata
import traceback
import textwrap
import aiohttp
import inspect
import asyncio
import time
import re
import io
import os
import random
from mtranslate import translate
from io import BytesIO
import string

class skid: 
     def __init__(self, bot):
          self.bot = bot
          self._last_result = None
          self.lang_conv = load_json('data/langs.json')
          self._last_embed = None
          self._rtfm_cache = None
          self._last_google = None
          
     @commands.command(aliases=['bn'])
     async def binary(self, ctx, number:int = None):
         if number is None:
             await ctx.send('Enter a number :D')
         else:
             await ctx.send(bin(number)[2:])
          
     @commands.command()
     async def getems(self, ctx):
         '''gets all emojis in a server'''
         l = []
         for e in ctx.guild.emojis:
             name = e.name+ " " + "{}".format(e)
             l.append (name)
         emo = ' '.join(l)
         await ctx.send(emo)
     
     @commands.command(pass_context=True, hidden=True, name='eval')
     async def _eval(self, ctx, *, body: str):
         """Evaluates python code"""

         env = {
             'bot': self.bot,
             'ctx': ctx,
             'channel': ctx.channel,
             'author': ctx.author,
             'guild': ctx.guild,
             'message': ctx.message,
             '_': self._last_result,
             'source': inspect.getsource
         }

         env.update(globals())

         body = self.cleanup_code(body)
         #await self.edit_to_codeblock(ctx, body)
         stdout = io.StringIO()
         err = out = None

         to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

         try:
             exec(to_compile, env)
         except Exception as e:
             err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
             return await err.add_reaction('\u2049')

         func = env['func']
         try:
             with redirect_stdout(stdout):
                 ret = await func()
         except Exception as e:
             value = stdout.getvalue()
             err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
         else:
             value = stdout.getvalue()
             if ret is None:
                 if value:
                     try:
                         out = await ctx.send(f'```py\n{value}\n```')
                     except:
                         paginated_text = ctx.paginate(value)
                         for page in paginated_text:
                             if page == paginated_text[-1]:
                                 out = await ctx.send(f'```py\n{page}\n```')
                                 break
                             await ctx.send(f'```py\n{page}\n```')
             else:
                 self._last_result = ret
                 try:
                     out = await ctx.send(f'```py\n{value}{ret}\n```')
                 except:
                     paginated_text = ctx.paginate(f"{value}{ret}")
                     for page in paginated_text:
                         if page == paginated_text[-1]:
                             out = await ctx.send(f'```py\n{page}\n```')
                             break
                         await ctx.send(f'```py\n{page}\n```')

         if out:
             await out.add_reaction('\u2705') #tick
         if err:
             await err.add_reaction('\u2049') #x
            
     def cleanup_code(self, content):
         """Automatically removes code blocks from the code."""
         # remove ```py\n```
         if content.startswith('```') and content.endswith('```'):
             return '\n'.join(content.split('\n')[1:-1])

         # remove `foo`
         return content.strip('` \n')

     def get_syntax_error(self, e):
         if e.text is None:
             return f'```py\n{e.__class__.__name__}: {e}\n```'
         return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'

     @commands.command()
     async def translate(self, ctx, language, *, phrase):
         translated = await ctx.bot.loop.run_in_executor(None, translate, language, phrase)
         await ctx.send(translated)

     
     @commands.command()
     async def getchanid(self, ctx):
         lel = ctx.channel.id
         await ctx.send(lel) 
          
     @commands.command()
     async def cato(self, ctx):
         await ctx.message.delete()
         await ctx.send(file = discord.File('4A583EDC-0A6F-47D8-8D3F-F4EDD06E2BB7.gif'))

     def getColor(self, colorHex):
        return discord.Colour(int(f'0x{colorHex}', 16))

     def randomcolor(self):
       color = ''.join([random.choice(string.hexdigits) for _ in range(6)])
       return self.getColor(color)  

     @commands.command()
     async def rc(self, ctx):
        '''Generates a random color'''
        file = io.BytesIO()
        color = self.randomcolor()
        Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
        file.seek(0)
        em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
        em.set_image(url='attachment://color.png')
        await ctx.send(file=discord.File(file, 'color.png'), embed=em)
          
     @commands.command()
     async def plt(self, ctx, *args):
        """PigLatin Translator"""
        for i in args:
            word = i
            py = "ay"
            first_word = word[0]
            if i is None:
                await ctx.send("Type something O:")
            else:
                new_word = word[1:len(word)]
                new_word = new_word + first_word + py
                em = discord.Embed(color = 0xffd500)
                em.description = ''.join(new_word)
        await ctx.send(embed = em)
        
            
        

     
def setup(bot):
   bot.add_cog(skid(bot))     
