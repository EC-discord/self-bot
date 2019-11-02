import discord
import asyncio
import random
import emoji
import json
from discord.ext import commands
from ext.colours import ColorNames
from PIL import Image
import io
import typing


class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.emoji_converter = commands.EmojiConverter()
        self.emoji_list = []
        
    @commands.command(aliases = ["as"])
    async def antisnipe(self, ctx):
        """deletes your previous message and prevents bots from sniping it"""
        await ctx.message.edit(content = " ")
        await ctx.message.delete()
        async for m in ctx.channel.history(limit = 100):
            if m.author.id == ctx.author.id:
                await m.edit(content = " ")
                await m.delete()
                break
        
    @commands.command()
    async def hexcode(self, ctx, *, role: discord.Role):
        await ctx.send(f"{role.name} : {role.color}")

    @commands.command(aliases = ["em"])
    async def embed(self, ctx, color: typing.Optional[discord.Color] = None, *, text):
        '''embed messages
        Parameters
        • text - the text to embed
        • color - the color of the embed, random color is used if left empty'''
        em = discord.Embed(color=color or random.randint(0, 0xFFFFFF))
        em.description = text
        await ctx.send(embed=em)
        await ctx.message.delete()
    
    @commands.command(aliases = ["rr"])
    async def randomreact(self, ctx, message_no: int, no_of_reactions: int = 20, *, server = None):
        '''react to a message with random emojis
        Parameters
        • message_no - the index of the message to react to
        • no_of_reactions - amount of random emojis to react with, defaults to 20
        • server - the server from which to choose the emojis to react with, defaults to global emojis
        '''
        self.emoji_list = []
        await ctx.message.delete()
        if server is None:
          self.emoji_list = [emoji for emoji in self.bot.emojis if emoji.name.startswith("GW")]
        elif server:
          server = discord.utils.find(lambda s: server in s.name.lower(), self.bot.guilds)
          self.emoji_list = [emoji for emoji in server.emojis if not emoji.animated]
        for index, message in enumerate(await ctx.channel.history(limit = 30).flatten()):
          if index != message_no:
            continue
          for i in range(no_of_reactions):
            emoji = random.choice(self.emoji_list)
            await message.add_reaction(emoji)
            self.emoji_list.remove(emoji)
          break
          
    @commands.command()
    async def react(self, ctx, message_no: typing.Optional[int] = 1, *, emojis):
        '''react to a specified message with emojis
        Parameters
        • message_no - the index of the message to react to
        • emojis - the names of the emojis to react with'''
        history = await ctx.channel.history(limit = 30).flatten()
        message = history[messageNo]
        async for emoji in self.validate_emojis(ctx, emojis):
            await message.add_reaction(emoji)
        await ctx.message.delete()

    async def validate_emojis(self, ctx, *reactions):
        '''
        Checks if an emoji is valid otherwise,
        tries to convert it into a custom emoji
        '''
        for emote in reactions:
            if emote in emoji.UNICODE_EMOJI:
                yield emote
            else:
                try:
                    yield await self.emoji_converter.convert(ctx, emote)
                except commands.BadArgument:
                    pass

    @commands.command(aliases=['color', 'colour', 'sc'])
    async def get_color(self, ctx, *, color: discord.Colour):
        '''displays a color from its name or hex value
        Parameters
        • color - the name or hexcode of the color to display
        '''
        file = io.BytesIO()
        Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
        file.seek(0)
        em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
        em.set_image(url='attachment://color.png')
        await ctx.send(file=discord.File(file, 'color.png'), embed=em)

    @commands.command(name='emoji', aliases=['e'])
    async def _emoji(self, ctx, size: typing.Optional[int] = None, emoji, emoji_no: int = 1):
        '''displays an enlarged pic of an emoji
        Parameters
        • size = the size of the image to display
        • emoji - The name(case sensitive) or id of the emoji
        • emoji_no - which emoji to choose from incase there is more than one, defaults to the first
        '''
        emoji = tuple(filter(lambda em: (emoji in em.name) or (emoji == em.id), self.bot.emojis))[emoji_no-1]
        async with ctx.session.get(f"{emoji.url}"+f"?size={size if size else ' '}") as resp:
            image = await resp.read()
        if emoji.animated:
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, "emote.gif"))
        else:
            with io.BytesIO(image) as file:
                await ctx.send(file = discord.File(file, "emote.png"))
        await ctx.message.delete()
                
    @commands.command()
    async def textreact(self, ctx, messageNo: typing.Optional[int] = 1, *, text):
        """reacts to a message with emojis according to the text
        Parameter
        • messageNo - the number of the message to react to
        • text - the text to react with
        """
        text = (c for c in text.lower())
        emotes = {"a" : "🇦", "b" : "🇧", "c" : "🇨", "d" : "🇩", "e" : "🇪", "f" : "🇫", "g" : "🇬", "h" : "🇭",
                  "i" : "🇮", "j" : "🇯", "k" : "🇰", "l" : "🇱", "m" : "🇲", "n" : "🇳", "o" : "🇴", "p" : "🇵",
                  "q" : "🇶", "r" : "🇷", "s" : "🇸", "t" : "🇹", "u" : "🇺", "v" : "🇻", "w" : "🇼", "x" : "🇽",
                  "y" : "🇾", "z" : "🇿"}
        for i, m in enumerate(await ctx.channel.history(limit = 100).flatten()):
            if messageNo == i:
              for c in text:
                  await m.add_reaction(f"{emotes[c]}")
              break
        await ctx.message.delete()
        
    @commands.command()
    async def textemote(self, ctx, *, text):
        """convert text into emojis
        Parameters
        • text - the text to turn into emojis
        """
        await ctx.message.delete()
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

def setup(bot):
    bot.add_cog(misc(bot))
