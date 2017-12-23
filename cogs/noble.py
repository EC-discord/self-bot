'''
~
witten by Noble#5242(Banned) (using PIL) feel free to edit and make it better.

'''
from __future__ import division
import discord
import operator
import base64
import asyncio
import codecs
import random
import pyimgflip
import time
import datetime
import io
import aiohttp
import urllib.request
import re
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
from bs4 import BeautifulSoup
from sympy import solve
from PIL import Image,ImageFilter,ImageDraw,ImageFont
from discord.ext import commands
from discord.ext import commands
from ext.utility import parse_equation
from ext.colours import ColorNames
from random import randint, choice




class Noble:
    def __init__(self, bot):
        self.bot = bot
        self.stopwatches = {}

    @commands.command()
    async def textgif(self,ctx,*,args):#EC DO NOT COPY PASTE THIS INTO A BOT! I WILL KEEL YOU IF YOU DO!
        '''Turn TEXT to GIF'''
        img = Image.new('RGB', (500, 45),"red")
        d = ImageDraw.Draw(img)
        c = 0
        length = int(len(args))
        font = ImageFont.truetype('Tabitha.ttf', 27)
        for m in range(length):
            x = 9
            d.text((x+c, 5), args[m], fill=(255, 255, 255), font = font)
            img.save('{}.png'.format(m))
            c += 12
        gif_name = 'content'
        fps = 10
        file_list = glob.glob('*.png') # Get all the pngs in the current directory
        list.sort(file_list) # Sort the images by #, this may need to be tweaked for your use case
        clip = mpy.ImageSequenceClip(file_list, fps=fps)
        clip.write_gif('{}.gif'.format(gif_name), fps=fps)
        await ctx.send(file=discord.File('content.gif'))
        await ctx.message.delete()
        for f in glob.glob("*.png"):
            os.remove(f)

    @commands.command()
    async def pil(self, ctx,args, *,member : discord.Member=None):
        '''A SIMPLE DEMO FOR WELCOMING (DEV)'''
        server = ctx.guild
        user = member or ctx.message.author
        avi = user.avatar_url
        url = avi
        response = requests.get(url, stream=True)
        with open('img.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        img = Image.open("img.png")
        img.thumbnail((200, 200))
        new_im = Image.new("RGBA", (400,400))
        img.thumbnail((150,150))
        new_im.paste(img,(100,100))
        font = ImageFont.truetype('arial.ttf', 19)
        xoff, yoff = (10,5)
        d = ImageDraw.Draw(new_im)
        d.text((90, 280), args, fill="white",font = font)
        new_im.save("on_test.png")
        await ctx.send(file=discord.File('on_test.png'))
        await ctx.message.delete()

    @commands.command()
    async def pictext(self,ctx,*,args):
        '''Turn Text to PIC'''
        font = ImageFont.truetype('arial.ttf', 21)
        xoff, yoff = (10,5)
        img = Image.new('RGB', (500, 45),'black')
        d = ImageDraw.Draw(img)
        d.text((9, 5), args, fill="green",font = font)
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
    async def decode(self,ctx,*,args):
        '''Decode to ascii'''
        strOne = ("%s" % args).encode("ascii")
        pad = len(strOne)%4
        strOne += b"="*pad
        encoded_stuff = codecs.decode(strOne.strip(),'base64')
        decoded_stuff = str(encoded_stuff)
        decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
        await ctx.message.delete()
        await ctx.send(content = "{}".format(decoded_stuff))

    @commands.command()
    async def stopwatch(self, ctx):
        """Starts/stops stopwatch"""
        author = ctx.author
        if not author.id in self.stopwatches:
            self.stopwatches[author.id] = int(time.perf_counter())
            await ctx.send(author.mention + " Stopwatch started!")
        else:
            tmp = abs(self.stopwatches[author.id] - int(time.perf_counter()))
            tmp = str(datetime.timedelta(seconds=tmp))
            await ctx.send(author.mention + " Stopwatch stopped! Time: **" + tmp + "**")
            self.stopwatches.pop(author.id, None)

    @commands.command()
    async def memeit(self, ctx, args1,args2):
        'MEME IT! memeit [text1] [text2]'
        api = pyimgflip.Imgflip(username='xjcn6iokow', password='xjcnb6i0k0w')
        memes = api.get_memes()
        meme = random.choice(memes)
        #print("Generating a meme from template: " + meme.name)
        if args1 == None and args2 == None:
            result = api.caption_image(meme, "I forget to add", "Captions!")
        else:
            result = api.caption_image(meme, "{}".format(args1), "{}".format(args2))
        #print("Meme available at URL: " + result['url'])
        em = discord.Embed()
        em.set_image(url = result['url'])
        try:
            await ctx.send(embed = em)
            await ctx.message.delete()
        except:
            await ctx.send(result['url'])
            await ctx.message.delete()

    @commands.command()
    async def disabled(self,ctx,*, member: discord.Member = None):
        'Make A disabled MEME Image (one pic only) XD'
        server = ctx.guild
        user = member or ctx.message.author
        avi = user.avatar_url
        url = '{}'.format(avi)
        response = requests.get(url, stream=True)
        with open('img2.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        img = Image.open("img2.png")
        new_im = Image.open("disability.jpg")
        img.thumbnail((98,98))
        new_im.paste(img,(318,216))
        new_im.save("disabled.jpg")
        await ctx.message.delete()
        await ctx.send(file=discord.File('disabled.jpg'))

    @commands.command()
    async def replycmd(self, ctx):
        'Other commands from a different worker run'
        ncommands = "New Commands: `noble!set [online/offline]`, `noble!status`"
        await ctx.send(ncommands)

    @commands.command()
    async def kington(self, ctx,*,args):
        'TEXT TO KLINGTON XD'
        URL = "http://mrklingo.freeshell.org/uta/index.php"
        regex = re.compile(r"-{12}\s+(.+?)\s+\-{12}", re.MULTILINE)
        cache = {}

        def translate(phrase):
            try:
                return cache[phrase]
            except KeyError:
                pass

            handle = urllib.request.urlopen(URL, urllib.parse.urlencode({'eng' : phrase, 'language' : 'klingon'}).encode("utf-8"))
            try:
                text = handle.read()
            except:
                return phrase

            match = regex.search(text.decode("utf-8"))
            if not match:
                return phrase

            cache[phrase] = match.group(1)
            return match.group(1)

        word = translate(args)
        await ctx.send(word)
        await ctx.message.delete()



def setup(bot):
    bot.add_cog(Noble(bot))
