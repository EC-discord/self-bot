import discord
from discord.ext import commands
from contextlib import redirect_stdout
from ext.utility import load_json
from PIL import Image
import traceback
import textwrap
import asyncio
import io
import random
import colorsys
import inspect

class skid(commands.Cog): 
     def __init__(self, bot):
          self.bot = bot
          self._last_result = None
          self.text_flip = {}
          self.char_list = "!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}"
          self.alt_char_list = "{|}zʎxʍʌnʇsɹbdouɯlʞɾᴉɥƃɟǝpɔqɐ,‾^[\]Z⅄XMΛ∩┴SɹQԀONW˥ʞſIHפℲƎpƆq∀@¿<=>;:68ㄥ9ϛㄣƐᄅƖ0/˙-'+*(),⅋%$#¡"[::-1]
          for idx, char in enumerate(self.char_list):
              self.text_flip[char] = self.alt_char_list[idx]
              self.text_flip[self.alt_char_list[idx]] = char
               
     @commands.command()
     async def eml(self, ctx, no_of_lines: int = 4, delay: int = 0):
         """displays lines in embeds
         Parameters
         • no_of_lines - how many lines to display, defaults to 4
         • delay - delay between sending lines, defaults to 0
         """
         for _ in range(no_of_lines):
              await ctx.invoke(self.bot.get_command("rc"), 100, 5, False)
     
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
     async def spam(self, ctx, text: str, spam_frequency: int, *spam_delay: int):
         spam_delay = list(spam_delay)
         await ctx.message.delete()
         for i in range(spam_frequency):
             await ctx.send(text)
             await asyncio.sleep(random.choice([num for num in spam_delay]))
     
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
         stdout = io.StringIO()
         err = out = None

         to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

         try:
             exec(to_compile, env)
         except Exception as e:
             err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
             return await err.add_reaction('❌')

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
             await out.add_reaction('✔')
         if err:
             await err.add_reaction('❌')
            
     def cleanup_code(self, content):
         """Automatically removes code blocks from the code."""
         if content.startswith('```') and content.endswith('```'):
             return '\n'.join(content.split('\n')[1:-1])
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
     async def rc(self, ctx, width = 200, height = 90, show_hexcode = True):
        '''Generates a random color'''
        file = io.BytesIO()
        color = self.randomcolor()
        Image.new('RGB', (width, height), color.to_rgb()).save(file, format='PNG')
        file.seek(0)
        em = discord.Embed(color=color)
        if show_hexcode:
          em.title = f'Showing Color: {str(color)}'
        em.set_image(url='attachment://color.png')
        await ctx.send(file=discord.File(file, 'color.png'), embed=em)
     
def setup(bot):
   bot.add_cog(skid(bot))
