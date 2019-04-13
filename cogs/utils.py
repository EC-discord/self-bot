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
    async def translate(self, ctx, language, *, text):
        """translates the string into a given language
        __**Parameters**__
        • language - the language to translate to
        • text - the text to be translated
        """
        await ctx.send(translate(text, language))
        
    @commands.command()
    @commands.has_permissions(manage_emojis = True)
    async def addemoji(self, ctx, emoji_name, emoji_link = '', *roles : discord.Role):
        """Add an emoji to a server
        __**Parameters**__
        • emoji_name – The emoji name. Must be at least 2 characters
        • emoji_link – The url or attachment of an image to turn into an emoji
        • roles – A list of Roles that can use this emoji (case sensitive). Leave empty to make it available to everyone
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
        "Deletes an emoji"
        await emoji.delete()
        await ctx.send(content = f"Deleted emoji : {emoji.name}", delete_after = 2)
        
    @commands.command()
    async def editemoji(self, ctx, emoji : discord.Emoji, new_name):
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
    async def nick(self, ctx, user : discord.Member, *, nickname : str = None):
        await user.edit(nick = nickname)
        nickname = nickname or user.name
        await ctx.send(f"Changed {user.name}'s nickname to {nickname}")
    
    @commands.command()
    async def cpres(self, ctx, Type : str = "playing", *, message : str = None):
        """Sets a presence
        __**Parameters**__
        • Type - "playing", "streaming", "listeningto" or "watching", defaults to playing
        • message - The message to display as presence
        """
        types = {"playing" : "Playing", "streaming" : "Streaming", "listeningto" : "Listening to", "watching" : "Watching"}
        if message is None:
            await self.bot.change_presence(activity = message, afk = True)
        else:
            if Type == "playing":
                await self.bot.change_presence(activity=discord.Game(name=message), afk = True)
            elif Type == "streaming":
                await self.bot.change_presence(activity=discord.Streaming(name=message, url=f'https://twitch.tv/{message}'), afk = True)
            elif Type == "listeningto":
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=message), afk = True)
            elif Type == "watching":
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=message), afk = True)
            em = discord.Embed(color=0xffd500, title="Presence")
            em.description = f"Presence : {types[Type]} {message}"
            if ctx.author.guild_permissions.embed_links:
                await ctx.send(embed = em)
            else:
                await ctx.send(f"Presence : {types[Type]} {message}")
            
    @commands.command()
    async def clear(self, ctx, *, serverid = "all"):
        '''Marks messages from selected servers as read'''
        if serverid != None:
            if serverid == 'all':
                for guild in self.bot.guilds:
                    await guild.ack()
                await ctx.send('Cleared all unread messages', delete_after = 2)
                return
            try:
                serverid = int(serverid)
            except:
                await ctx.send('Invalid Server ID')
                return
            server = discord.utils.get(self.bot.guilds, id=int(serverid))
            if server == None:
                await ctx.send('Invalid Server ID')
                return
            await server.ack()
            await ctx.send(f'All messages marked read in {server.name}!')
            return
        for guild in self.bot.guilds:
            if guild.id in emotes_servers:
                await guild.ack()
        await ctx.send('All messages marked read in specified servers!')

    @commands.command()
    async def choose(self, ctx, *, choices: commands.clean_content):
        '''choose! use , in between'''
        choices = choices.split(',')
        choices[0] = ' ' + choices[0]
        await ctx.send(str(random.choice(choices))[1:])
        
    @commands.command()
    async def picsu(self, ctx, *, member : discord.Member = None):
        """gets the Display Picture of a user
        __**Parameters**__
        • member – The tag, name or id of the user
        """
        format = None
        member = member or ctx.author
        if member.is_avatar_animated() != True:
	        format = "png"
        avatar = member.avatar_url_as(format = format if format is not "gif" else None)
        async with ctx.session.get(str(avatar)) as resp:
            image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file = discord.File(file, f"DP.{format}"))
            
    @commands.command(aliases = ["sicon", "si"])
    async def servericon(self, ctx, *, guild = None):
        """gets a server's icon
        __**Parameters**__
        • guild - The name(case sensitive) or id of the guild/server"""
        if guild is None:
            guild = ctx.guild
        elif type(guild) == int:
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
