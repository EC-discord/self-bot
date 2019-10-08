import discord
import base64
import asyncio
import random
import datetime
import os
import json
import glob
import moviepy.editor as mpy
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
from ext.colours import ColorNames
import codecs


class noble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def textgif(self,ctx,*,args):
        '''Turn TEXT to GIF'''
        img = Image.new('RGB', (500, 45),"black")
        d = ImageDraw.Draw(img)
        c = 0
        font = ImageFont.truetype('./Tabitha.ttf', 27)
        for m in range(len(args)):
            x = 9
            d.text((x+c, 5), args[m], fill=(255, 255, 255), font = font)
            img.save(f'{m}.png')
            c += 13
        file_list = glob.glob('*.png')
        list.sort(file_list)
        clip = mpy.ImageSequenceClip(file_list, fps=10)
        clip.write_gif('content.gif', fps=10)
        await ctx.send(file=discord.File('content.gif'))
        await ctx.message.delete()
        for f in glob.glob("*.png"):
            os.remove(f)

    @commands.command()
    async def pictext(self,ctx,*,args):
        '''Turn Text to PIC'''
        font = ImageFont.truetype('./Tabitha.ttf', 21)
        xoff, yoff = (10,5)
        img = Image.new('RGB', (500, 45),'black')
        d = ImageDraw.Draw(img)
        d.text((9, 5), args, fill="white",font = font)
        img.save('content.jpeg')
        await ctx.message.delete()
        await ctx.send(file=discord.File('content.jpeg'))

    @commands.command()
    async def encode(self,ctx,*,args):
        '''Encode ascii Text to base64'''
        decoded_stuff = base64.b64encode('{}'.format(args).encode('ascii'))
        encoded_stuff = str(decoded_stuff)
        encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
        await ctx.message.delete()
        await ctx.send(content = "{}".format(encoded_stuff))

    @commands.command()
    async def decode(self,ctx,*,args : str):
        '''Decode to ascii'''
        strOne = (args).encode("ascii")
        pad = len(strOne)%4
        strOne += b"="*pad
        encoded_stuff = codecs.decode(strOne.strip(),'base64')
        decoded_stuff = str(encoded_stuff)
        decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
        await ctx.message.delete()
        await ctx.send(content = "{}".format(decoded_stuff))

def setup(bot):
    bot.add_cog(noble(bot))
