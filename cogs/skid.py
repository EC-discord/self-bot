import discord
from discord.ext import commands
from discord.ext.commands import TextChannelConverter
from contextlib import redirect_stdout
from ext.utility import load_json
from urllib.parse import quote as uriquote
from ext import embedtobox
from PIL import Image
import traceback
import textwrap
import aiohttp
import inspect
import asyncio
import time
import os
import io
import random
from mtranslate import translate
from io import BytesIO
import string
import colorsys

class skid: 
     def __init__(self, bot):
          self.bot = bot
          self._last_result = None
          self.lang_conv = load_json('data/langs.json')
          self._last_embed = None
          self._rtfm_cache = None
          self._last_google = None
          self.text_flip = {}
          self.char_list = "!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}"
          self.alt_char_list = "{|}zʎxʍʌnʇsɹbdouɯlʞɾᴉɥƃɟǝpɔqɐ,‾^[\]Z⅄XMΛ∩┴SɹQԀONW˥ʞſIHפℲƎpƆq∀@¿<=>;:68ㄥ9ϛㄣƐᄅƖ0/˙-'+*(),⅋%$#¡"[::-1]
          for idx, char in enumerate(self.char_list):
              self.text_flip[char] = self.alt_char_list[idx]
              self.text_flip[self.alt_char_list[idx]] = char
     
     @commands.command()
     async def textflip(self, ctx, *, message):
         result = " "
         for char in message:
             if char in self.text_flip:
                 result += self.text_flip[char]
             else:
                 result += char
         await ctx.message.edit(content=result[::-1])
    
     @commands.command()
     async def spam(self, ctx, text : str, spam_frequency : int, *spam_delay : int):
         spam_delay = list(spam_delay)
         await ctx.message.delete()
         for i in range(spam_frequency):
             await ctx.send(text)
             await asyncio.sleep(random.choice([num for num in spam_delay]))
          
     @commands.command(aliases=['bn'])
     async def binary(self, ctx, number:int = None):
         if number is None:
             await ctx.send('Enter a number :D')
         else:
             await ctx.send(bin(number)[2:])
          
     @commands.command()
     async def getemojis(self, ctx):
         '''gets all emojis in a server'''
         emoji_list = [e for e in ctx.guild.emojis if not emoji.animated]
         await ctx.send(emoji_list)
     
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
          
     def getColor(self, colorHex):
        colorHex = str(colorHex)
        return discord.Colour(int(f'0x{colorHex[1:]}', 16))

     def randomcolor(self):
       values = [int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1)]
       color = discord.Color.from_rgb(*values)
       return self.getColor(color)  

     @commands.command()
     async def rc(self, ctx):
        '''Generates a random color'''
        file = io.BytesIO()
        color = self.randomcolor()
        Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
        file.seek(0)
        em = discord.Embed(color=color , title=f'Showing Color: {str(color)}')
        em.set_image(url='attachment://color.png')
        await ctx.send(file=discord.File(file, 'color.png'), embed=em)
          
     @commands.command()
     async def plt(self, ctx, *words):
        """PigLatin Translator"""
        translated = [w[1:] + w[0] + "ay" for w in words]
        em = discord.Embed(color = 0xffd500)
        em.description = " ".join(translated)
        await ctx.send(embed = em)
            
     @commands.command()
     async def haxu(self, ctx, limit : int = 10):
         async for message in ctx.channel.history(limit = limit):
             if message.author == self.bot.user:
                await message.edit(content = "ㅤ ")
                await asyncio.sleep(1)
                await message.delete()
           
     @commands.command()
     async def getrekt(self, ctx, role : discord.Role):
          "kicks all members having the specified role"
          for member in role.members:
              await member.kick()
     
def setup(bot):
   bot.add_cog(skid(bot))     
