import discord
from discord.ext import commands
from discord.ext.commands import TextChannelConverter
from ext.utility import load_json
from urllib.parse import quote as uriquote
from mtranslate import translate
from ext import fuzzy
from ext import embedtobox
from PIL import Image
import traceback
import aiohttp
import asyncio
import time
import re
import random


class Utility:
    def __init__(self, bot):
        self.bot = bot
        self.lang_conv = load_json('data/langs.json')
    
    @commands.command()
    async def translate(self, ctx, language, *, text):
        await ctx.send(translate(text, language))
       
    @commands.command()
    async def edit(self, ctx, messageNo, *, new_message):
        messageId = 0
        async for message in ctx.channel.history(limit = 30):
            if message.author.id == ctx.message.author.id and messageNo == messageId:
                await message.edit(content = new_message)
                break
            elif messageNo == messageId and message.author.id != ctx.message.author.id:
                await ctx.send(content = "you can't edit someone elses message", delete_after = 4)
                break
            if message.author.id == ctx.message.author.id:
                messageId += 1
            else:
                continue
            continue
        
    @commands.command()
    async def addemoji(self, ctx, emoji_name, emoji_link = ''):
        msg: discord.Message = ctx.message
        if ctx.author.guild_permissions.manage_emojis == True:
            if msg.attachments:
                image = msg.attachments[0]
            elif emoji_link:
                async with ctx.session.get(emoji_link) as resp:
                    image = await resp.read()
            else:
                await ctx.send("No valid emoji provided.")
                return
            created_emoji = await ctx.guild.create_custom_emoji(name = emoji_name, image = image)
            await ctx.send("Emoji {} created!".format(created_emoji))
        else:
            await ctx.send(content = "You do not have the **Manage emojis** perm", delete_after = 2)
     
    @commands.command()
    async def delemoji(self, ctx, name: str):
        "Deletes an emoji"
        emoji = discord.utils.get(ctx.guild.emojis, name = name)
        await emoji.delete()
        await ctx.send(content = f"Deleted emoji : {name}", delete_after = 2)
        
    @commands.command()
    async def editemoji(self, ctx, emoji_name, new_name):
        emoji = discord.utils.get(ctx.guild.emojis, name = emoji_name)
        await emoji.edit(name = new_name)
        await ctx.send(content = f"Edited emoji {emoji_name} to {new_name}")
    
    @commands.command(name='logout')
    async def _logout(self, ctx):
        '''
        restart bot
        '''
        await ctx.send('`Selfbot Logging out...`')
        await self.bot.logout()

    @commands.command(name='help')
    async def new_help_command(self, ctx, *commands : str):
        """get help cmds"""
        destination = ctx.message.author if self.bot.pm_help else ctx.message.channel

        def repl(obj):
            return self.bot._mentions_transforms.get(obj.group(0), '')

        # help by itself just lists our own commands.
        if len(commands) == 0:
            pages = await self.bot.formatter.format_help_for(ctx, self.bot)
        elif len(commands) == 1:
            # try to see if it is a cog name
            name = self.bot._mention_pattern.sub(repl, commands[0])
            command = None
            if name in self.bot.cogs:
                command = self.bot.cogs[name]
            else:
                command = self.bot.all_commands.get(name)
                if command is None:
                    await destination.send(self.bot.command_not_found.format(name))
                    return

            pages = await self.bot.formatter.format_help_for(ctx, command)
        else:
            name = self.bot._mention_pattern.sub(repl, commands[0])
            command = self.bot.all_commands.get(name)
            if command is None:
                await destination.send(self.bot.command_not_found.format(name))
                return

            for key in commands[1:]:
                try:
                    key = self.bot._mention_pattern.sub(repl, key)
                    command = command.all_commands.get(key)
                    if command is None:
                        await destination.send(self.bot.command_not_found.format(key))
                        return
                except AttributeError:
                    await destination.send(self.bot.command_has_no_subcommands.format(command, key))
                    return

            pages = await self.bot.formatter.format_help_for(ctx, command)

        if self.bot.pm_help is None:
            characters = sum(map(lambda l: len(l), pages))
            # modify destination based on length of pages.
            if characters > 1000:
                destination = ctx.message.author

        color = await ctx.get_dominant_color(ctx.author.avatar_url)

        for embed in pages:
            embed.color = color
            try:
                await ctx.send(embed=embed)
            except discord.HTTPException:
                em_list = await embedtobox.etb(embed)
                for page in em_list:
                    await ctx.send(page)
      
    @commands.command()
    async def nick(self, ctx, user : discord.Member, *, nickname : str = None):
        await user.edit(nick = nickname)
        await ctx.send("Changed {user.name}'s nickname to {nickname}")
    
    @commands.command()
    async def cpres(self, ctx, status : str, Type:str = "playing", *, message:str = None):
        '''Sets a custom presence, the Type argument can be "playing", "streaming", "listeningto" or "watching"
        status can be "online", "dnd", "idle", "invisible"
        Example : (prefix)cpres idle watching a movie'''
        types = {"playing" : "Playing", "streaming" : "Streaming", "listeningto" : "Listening to", "watching" : "Watching"}
        stats = {"online" : discord.Status.online, "dnd" : discord.Status.dnd, "idle" : discord.Status.idle, "invisible" : discord.Status.invisible}
        em = discord.Embed(color=0x6ed457, title="Presence")
        if message is None:
            await self.bot.change_presence(status=discord.Status.online, activity= message, afk = True)
        else:
            if Type == "playing":
                await self.bot.change_presence(status=stats[status], activity=discord.Game(name=message), afk = True)
            elif Type == "streaming":
                await self.bot.change_presence(status=stats[status], activity=discord.Streaming(name=message, url=f'https://twitch.tv/{message}'), afk = True)
            elif Type == "listeningto":
                await self.bot.change_presence(status=stats[status], activity=discord.Activity(type=discord.ActivityType.listening, name=message), afk = True)
            elif Type == "watching":
                await self.bot.change_presence(status=stats[status], activity=discord.Activity(type=discord.ActivityType.watching, name=message), afk = True)
            em.description = f"Presence : {types[Type]} {message}"
            if ctx.author.guild_permissions.embed_links:
                await ctx.send(embed = em)
            else:
                await ctx.send(f"Presence : {types[Type]} {message}")      

    @commands.command()
    async def clear(self, ctx, *, serverid = "all"):
        '''Marks messages from selected servers or emote servers as read'''
        if serverid != None:
            if serverid == 'all':
                for guild in self.bot.guilds:
                    await guild.ack()
                await ctx.send('Cleared all unread messages')
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
        await ctx.send('All messages marked read in emote servers!')

    @commands.command()
    async def choose(self, ctx, *, choices: commands.clean_content):
        '''choose! use , in between'''
        choices = choices.split(',')
        if len(choices) < 2:
            return await ctx.send('Not enough choices to pick from.')
        choices[0] = ' ' + choices[0]
        await ctx.send(str(random.choice(choices))[1:])
        
    @commands.command()
    async def picsu(self, ctx, *, member : discord.Member = None):
        """gets the profile pic of the user"""
        await ctx.message.delete()
        mem = member or ctx.author
        avatar = mem.avatar_url_as(static_format='png', size=512)
        await ctx.send(avatar)

def setup(bot):
    bot.add_cog(Utility(bot))
