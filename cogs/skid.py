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

class skid: 
     def __init__(self, bot):
          self.bot = bot
          self._last_result = None
          self.lang_conv = load_json('data/langs.json')
          self._last_embed = None
          self._rtfm_cache = None
          self._last_google = None
     
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

     def eng(self, text):
         totranslate = (text)
         return translate(totranslate)
     
     @commands.command()
     async def en(self, ctx, *,args:str = None):
         translated = self.en(args)
         await ctx.send(translated)
     
     @commands.command()
     async def getchanid(self, ctx):
         lel = ctx.channel.id
         await ctx.send(lel)
          
     @commands.command()
     async def work(self, ctx):
         while True:
             channel = get_channel(id = 337337493592735764)
             await channel.send('!work')
             await asyncio.sleep(1)
             await channel.send('!deposit all')
             await asyncio.sleep(3600)
         
         
                    
     
     
def setup(bot):
   bot.add_cog(skid(bot))     
