import discord
import asyncio
import random
import emoji
from discord.ext import commands
from PIL import Image
import io
import typing
import aiohttp

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.emoji_converter = commands.EmojiConverter()
        self.emoji_list = []
        
    @commands.command(aliases = ["tt"])
    async def triggertyping(self, ctx, duration: int, channel: discord.TextChannel = None):
        """sends a typing indicator for a specified amount of time
        Parameters
        • duration - how long to keep the typing indicator running
        • channel - which channel to send the typing indicator in, defaults to the current channel
        """
        channel = channel or ctx.channel
        async with channel.typing():
            await asyncio.sleep(duration)
        
    @commands.command()
    async def hexcode(self, ctx, *, role: discord.Role):
        """returns the hexcode of a role's color
        Parameters
        • role - the role to display the color of
        """
        await ctx.send(f"{role.name} : {role.color}")

    @commands.command(aliases = ["em"])
    async def embed(self, ctx, color: typing.Optional[discord.Color] = None, *, text):
        '''embed text
        Parameters
        • text - the text to embed
        • color - the color of the embed, a random color is used if left empty
        '''
        em = discord.Embed(color=color or random.randint(0, 0xFFFFFF))
        em.description = text
        await ctx.send(embed=em)
        await ctx.message.delete()
    
    @commands.command(aliases = ["rr"])
    async def randomreact(self, ctx, message_no: int, no_of_reactions: typing.Optional[int] = 20, *, server: str = None):
        '''react to a message with random emojis
        Parameters
        • message_no - the index of the message to react to
        • no_of_reactions - amount of random emojis to react with, defaults to 20
        • server - the server from which to choose the emojis to react with, defaults to global emojis
        '''
        message_no-=1
        server = server.lower() if server else server
        self.emoji_list = []
        await ctx.message.delete()
        if server is None:
          self.emoji_list = [emoji for emoji in self.bot.emojis if emoji.name.startswith("GW")]
        elif server:
          s = discord.utils.find(lambda s: server in s.name.lower(), self.bot.guilds)
          self.emoji_list = [emoji for emoji in s.emojis if not emoji.animated]
        for index, message in enumerate(await ctx.channel.history(limit = 30).flatten()):
          if index != message_no:
            continue
          for i in range(no_of_reactions):
            emoji = self.emoji_list.pop(self.emoji_list.index(random.choice(self.emoji_list)))
            await message.add_reaction(emoji)
            await asyncio.sleep(0.1)
          break
          
    @commands.command()
    async def react(self, ctx, message_no: typing.Optional[int] = 1, *, emojis):
        '''react to a specified message with emojis
        Parameters
        • message_no - the index of the message to react to
        • emojis - the emojis to react with
        '''
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
    async def getcolor(self, ctx, color: discord.Colour, width: int = 200, height: int = 90, show_hexcode = True):
        '''displays a color from its name or hex value
        Parameters
        • color - the name or hexcode of the color to display
        • width - width of the image to display, defaults to 200
        • height - height of the image to display, defaults to 90
        • show_hexcode - whether to display the hexcode of the color, defaults to True
        '''
        file = io.BytesIO()
        Image.new('RGB', (width, height), color.to_rgb()).save(file, format='PNG')
        file.seek(0)
        if show_hexcode:
            em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
        elif show_hexcode == False or "false":
            em = discord.Embed(color=color)
        em.set_image(url='attachment://color.png')
        await ctx.send(file=discord.File(file, 'color.png'), embed=em)

    @commands.command(name='emoji', aliases=['e'])
    async def _emoji(self, ctx, emoji: discord.Emoji, size: int=None):
        '''displays an enlarged pic of the emoji
        Parameters
        • size - the size of the image to display
        • emoji - The name(case sensitive) or id of the emoji
        '''
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{emoji.url}"+f"?size={size if size else ' '}") as resp:
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
        """reacts to a message with emojis corresponding to the text
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
        

def setup(bot):
    bot.add_cog(misc(bot))
