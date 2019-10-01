import discord
from discord.ext import commands
from ext.utility import load_json
from mtranslate import translate
from ext import embedtobox
from PIL import Image
import traceback
import aiohttp
import asyncio
import time
import random
import typing
import io

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lang_conv = load_json('data/langs.json')
        
    @commands.command()
    async def banner(self, ctx, *, guild = None):
        """gets a guild's banner image
        Parameters
        • guild - the name or id of the guild
        """
        if guild is None:
            guild = ctx.guild
        elif type(guild) == int:
            guild = discord.utils.get(self.bot.guilds, id = guild)
        elif type(guild) == str:
            guild = discord.utils.get(self.bot.guilds, name = guild)
        banner = guild.banner_url_as(format = "png")
        async with ctx.session.get(str(banner)) as resp:
            image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file = discord.File(file, "banner.png"))
        
    @commands.command()
    async def translate(self, ctx, language, *, text):
        """translates the string into a given language
        Parameters
        • language - the language to translate to
        • text - the text to be translated
        """
        await ctx.send(translate(text, language))
        await asyncio.sleep(2)
        await ctx.message.delete()
        
    @commands.command()
    @commands.has_permissions(manage_emojis = True)
    async def addemoji(self, ctx, emoji_name, emoji_link = '', *roles: discord.Role):
        """add an emoji to a server
        Parameters
        • emoji_name – The emoji name. Must be at least 2 characters
        • emoji_link – The url or attachment of an image to turn into an emoji
        • roles – A list of roles that can use this emoji. Leave empty to make it available to everyone
        """
        if ctx.message.attachments:
            emoji_link = ctx.message.attachments[0].url
            async with ctx.session.get(emoji_link) as resp:
                image = await resp.read()
        elif emoji_link:
            async with ctx.session.get(emoji_link) as resp:
                image = await resp.read()
        created_emoji = await ctx.guild.create_custom_emoji(name = emoji_name, image = image, roles = [r for r in roles if roles is not None])
        await ctx.send(f"Emoji {created_emoji} created!")
     
    @commands.command()
    async def delemoji(self, ctx, emoji: discord.Emoji):
        """deletes an emoji
        Parameters
        • emoji - the name or id of the emoji
        """
        await emoji.delete()
        await ctx.send(content = f"Deleted emoji : {emoji.name}", delete_after = 2)
        
    @commands.command()
    async def editemoji(self, ctx, emoji: discord.Emoji, new_name):
        """edits the name of an emoji
        Parameters
        • emoji - the name or id of the emoji
        • new_name - the new name to use for the emoji
        """
        await emoji.edit(name = new_name)
        await ctx.send(content = f"Edited emoji {emoji_name} to {new_name}", delete_after = 2)
    
    @commands.command(name='logout')
    async def _logout(self, ctx):
        '''
        restart the bot
        '''
        await ctx.send('`Selfbot Logging out`')
        await self.bot.logout()
      
    @commands.command()
    async def nick(self, ctx, user: discord.Member, *, nickname: str = None):
        """change a user's nickname
        Parameter
        • user - the name or id of the user
        • nickname - the nickname to change to
        """
        await user.edit(nick = nickname)
        nickname = nickname or user.name
        await ctx.send(f"Changed {user.name}'s nickname to {nickname}")
    
    @commands.command()
    async def cpres(self, ctx, Type: str = "playing", *, text: str = None):
        """sets a presence
        Parameters
        • Type - "playing", "streaming", "listeningto" or "watching", defaults to playing
        • text - The text to display as presence
        """
        types = {"playing" : "Playing", "streaming" : "Streaming", "listeningto" : "Listening to", "watching" : "Watching"}
        if text is None:
            await self.bot.change_presence(activity = text, afk = True)
        else:
            if Type == "playing":
                await self.bot.change_presence(activity=discord.Game(name=text), afk = True)
            elif Type == "streaming":
                await self.bot.change_presence(activity=discord.Streaming(name=text, url=f'https://twitch.tv/{text}'), afk = True)
            elif Type == "listeningto":
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=text), afk = True)
            elif Type == "watching":
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text), afk = True)
            em = discord.Embed(color=0xffd500, title="Presence")
            em.description = f"Presence : {types[Type]} {text}"
            if ctx.author.guild_permissions.embed_links:
                await ctx.send(embed = em)
            else:
                await ctx.send(f"Presence : {types[Type]} {text}")
            
    @commands.group(invoke_without_command=True)
    async def clear(self, ctx):
        """marks all messages from specified server as read"""
        if ctx.invoked_subcommand is None:
          for guild in self.bot.guilds:
            await guild.ack()
          await ctx.send('All messages marked read in specified servers!')
        await ctx.message.delete()
    
    @clear.command()
    async def name(self, ctx, *, server_name):
        """using the name of the server
        Parameter
        • server_name - the name of the server
        """
        server = discord.utils.find(lambda s: server_name in s.name.lower(), self.bot.guilds)
        await server.ack()
        await ctx.send(f"all messages marked read in {server.name}", delete_after = 2)
        await ctx.message.delete()
        
    @clear.command(name = "id")
    async def _id(self, ctx, server_id : int):
        """using the id of the server
        Parameter
        • server_id - the id of the server to mark as read
        """
        server = discord.utils.get(self.bot.guilds, id = server_id)
        await server.ack()
        await ctx.send(f"all messages marked read in {server.name}", delete_after = 2)
        await ctx.message.delete()

    @commands.command()
    async def choose(self, ctx, *, choices: commands.clean_content):
        '''choose! use , in between
        Parameters
        • choices - the choices to choose from separated using ,'''
        choices = choices.split(',')
        choices[0] = ' ' + choices[0]
        await ctx.send(str(random.choice(choices))[1:])
        
    @commands.command(aliases = ["a"])
    async def avatar(self, ctx, *, member: discord.Member = None):
        """gets the Display Picture of a user
        Parameters
        • member – The tag, name or id of the user
        """
        format = "gif"
        member = member or ctx.author
        if member.is_avatar_animated() != True:
	        format = "png"
        avatar = member.avatar_url_as(format = format if format is not "gif" else None)
        async with ctx.session.get(str(avatar)) as resp:
            image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file = discord.File(file, f"DP.{format}"))
            
    @commands.command(aliases = ["gicon", "gi"])
    async def guildicon(self, ctx, *, guild = None):
        """gets a guild's icon
        Parameters
        • guild - The name(case sensitive) or id of the guild/server"""
        if guild is None:
            guild = ctx.guild
        if type(guild) == int:
            guild = discord.utils.get(self.bot.guilds, id = guild)
        elif type(guild) == str:
            guild = discord.utils.get(self.bot.guilds, name = guild)
        icon = guild.icon_url_as(format = "png")
        async with ctx.session.get(str(icon)) as resp:
            image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file = discord.File(file, "icon.png"))
        
def setup(bot):
    bot.add_cog(Utility(bot))
