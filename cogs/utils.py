import discord
from discord.ext import commands
from ext.utility import load_json
from mtranslate import translate
import random
import io
import re
import aiohttp


class utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lang_conv = load_json('data/langs.json')

    @commands.command()
    async def setbanner(self, ctx, *, banner=None):
        """sets the guilds banner
        Parameters
        • banner - the attachment or url of the image to use as a banner
        """
        if ctx.message.attachments:
            image = await ctx.message.attachments[0].read()
        elif banner:
            async with aiohttp.ClientSession() as session:
                async with session.get(banner) as resp:
                    image = await resp.read()
        await ctx.guild.edit(banner=image)
        await ctx.send("Banner updated")

    @commands.command()
    async def setsplash(self, ctx, *, splash=None):
        """sets the guilds invite splash
        Parameters
        • splash - the attachment or url of the image to use as the invite splash
        """
        if ctx.message.attachments:
            image = await ctx.message.attachments[0].read()
        elif splash:
            async with aiohttp.ClientSession() as session:
                async with session.get(splash) as resp:
                    image = await resp.read()
        await ctx.guild.edit(splash=image)
        await ctx.send("Invite Splash updated")

    @commands.command()
    async def splash(self, ctx, *, guild=None):
        """gets a guild's invite splash(invite background)
        Parameters
        • guild - the name or id of the guild
        """
        if guild is None:
            guild = ctx.guild
        elif guild.isdigit() and len(guild) == 18:
            guild = discord.utils.get(self.bot.guilds, id=int(guild))
        elif type(guild) == str:
            guild = discord.utils.get(self.bot.guilds, name=guild)
        splash = await guild.splash_url_as(format="png").read()
        with io.BytesIO(splash) as f:
            await ctx.send(file=discord.File(f, "splash.png"))

    @commands.command()
    async def banner(self, ctx, *, guild=None):
        """gets a guild's banner image
        Parameters
        • guild - the name or id of the guild
        """
        if guild is None:
            guild = ctx.guild
        elif guild.isdigit() and len(guild) == 18:
            guild = discord.utils.get(self.bot.guilds, id=int(guild))
        elif type(guild) == str:
            guild = discord.utils.get(self.bot.guilds, name=guild)
        banner = await guild.banner_url_as(format="png").read()
        with io.BytesIO(banner) as f:
            await ctx.send(file=discord.File(f, "banner.png"))

    @commands.command()
    async def translate(self, ctx, language, *, text):
        """translates the string into a given language
        Parameters
        • language - the language to translate to
        • text - the text to be translated
        """
        await ctx.send(translate(text, language))

    @commands.command()
    async def addemoji(self, ctx, emoji_name, emoji_url=None):
        """adds an emoji to a server
        Parameters
        • emoji_name – the name of the emoji
        • emoji_url – the url or attachment of an image to turn into an emoji
        """
        if ctx.message.attachments:
            image = await ctx.message.attachments[0].read()
        elif emoji_url:
            async with aiohttp.ClientSession() as session:
                async with session.get(emoji_url) as resp:
                    image = await resp.read()
        emoji = await ctx.guild.create_custom_emoji(name=emoji_name, image=image)
        await ctx.send(f"Emoji {emoji.name} created!")

    @commands.command()
    async def delemoji(self, ctx, emoji: discord.Emoji):
        """deletes an emoji
        Parameters
        • emoji - the name or id of the emoji
        """
        name = emoji.name
        await emoji.delete()
        await ctx.send(content=f"Deleted emoji: {name}", delete_after=2)

    @commands.command()
    async def editemoji(self, ctx, emoji: discord.Emoji, new_name):
        """edits the name of an emoji
        Parameters
        • emoji - the name or id of the emoji
        • new_name - the new name to use for the emoji
        """
        emoji_name = emoji.name
        await emoji.edit(name=new_name)
        await ctx.send(content=f"Edited emoji {emoji_name} to {new_name}", delete_after=2)

    @commands.command(name='logout')
    async def _logout(self, ctx):
        """
        restart the bot
        """
        await ctx.send('`Selfbot Logging out`')
        await self.bot.logout()

    @commands.command()
    async def nick(self, ctx, user: discord.Member, *, nickname: str = None):
        """change a user's nickname
        Parameter
        • user - the name or id of the user
        • nickname - the nickname to change to
        """
        prevnick = user.nick or user.name
        await user.edit(nick=nickname)
        newnick = nickname or user.name
        await ctx.send(f"Changed {prevnick}'s nickname to {newnick}")

    @commands.command(aliases=["ca", "cactivity"])
    async def customactivity(self, ctx, Type: str = "playing", *, text: str = None):
        """sets a custom activity
        Parameters
        • Type - "playing", "streaming", "listeningto" or "watching", defaults to playing
        • text - The text to display as presence
        """
        types = {"playing": "Playing", "streaming": "Streaming", "listeningto": "Listening to", "watching":
            "Watching"}
        if text is None:
            await self.bot.change_presence(activity=text, afk=True)
        else:
            if Type == "playing":
                await self.bot.change_presence(activity=discord.Game(name=text), afk=True)
            elif Type == "streaming":
                await self.bot.change_presence(activity=discord.Streaming(name=text, url=f'https://twitch.tv/{text}'),
                                               afk=True)
            elif Type == "listeningto":
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
                                                                         name=text), afk=True)
            elif Type == "watching":
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text),
                                               afk=True)
            em = discord.Embed(color=0xffd500, title="Presence")
            em.description = f"Presence : {types[Type]} {text}"
            if ctx.author.guild_permissions.embed_links:
                await ctx.send(embed=em)
            else:
                await ctx.send(f"Presence : {types[Type]} {text}")

    @commands.command()
    async def choose(self, ctx, *, choices: commands.clean_content):
        """choose! use , in between
        Parameters
        • choices - the choices to choose from separated using ,"""
        choices = choices.split(',')
        choices[0] = ' ' + choices[0]
        await ctx.send(str(random.choice(choices))[1:])

    def get_user_from_global_cache(self, user):
        for u in self.bot.users:
            if user == u.name:
                return user

    @commands.command(aliases=["a", "pic"])
    async def avatar(self, ctx, *, user=None):
        """gets the display picture of a user
        Parameters
        • user – The tag, name or id of the user
        """
        user = user or ctx.author
        if type(user) != discord.Member:
            user = str(user)
            r = re.compile(r"@(.*#\d{4})|(\d{18})")
            r = r.search(user)
            if r:
                if r.group(2):
                    user = int(r.group(2))
                elif r.group(1):
                    user = r.group(1)
        if type(user) == str:
            user = ctx.guild.get_member_named(user)
        if user is None:
            user = self.get_user_from_global_cache(user)
        elif str(user).isdigit() and len(str(user)) == 18:
            user = await self.bot.fetch_user(user)
        if user.is_avatar_animated():
            format = "gif"
        else:
            format = "png"
        avatar = await user.avatar_url_as(format=format).read()
        with io.BytesIO(avatar) as file:
            await ctx.send(file=discord.File(file, f"DP.{format}"))
        await ctx.delete()

    @commands.command(aliases=["gi"])
    async def guildicon(self, ctx, *, guild=None):
        """gets a guild's icon
        Parameters
        • guild - The name(case sensitive) or id of the guild/server"""
        guild = guild or ctx.guild
        format = "png"
        if guild.isdigit() and len(guild) == 18:
            guild = discord.utils.get(self.bot.guilds, id=int(guild))
        elif type(guild) == str:
            guild = discord.utils.get(self.bot.guilds, name=guild)
        if guild.is_icon_animated():
            format = "gif"
        icon = await guild.icon_url_as(format=format).read()
        with io.BytesIO(icon) as file:
            await ctx.send(file=discord.File(file, f"icon.{format}"))


def setup(bot):
    bot.add_cog(utility(bot))
