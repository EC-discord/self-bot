import discord
from discord.ext import commands
import asyncio


class Mod(commands.Cog):
    """useful commands for moderation"""
    def __init__(self, bot):
        self.bot = bot

    async def format_mod_embed(self, ctx, user, success, method, duration = None, location=None):
        '''Helper func to format an embed to prevent extra code'''
        emb = discord.Embed()
        emb.set_author(name=method.title(), icon_url=user.avatar_url_as(static_format="png"))
        emb.color = await ctx.get_dominant_color(user.avatar_url)
        emb.set_footer(text=f'User ID: {user.id}')
        if success:
            if method == 'ban' or method == 'hackban':
                emb.description = f'{user} was just {method}ned.'
            else:
                emb.description = f'{user} was just {method}ed.'
        else:
            emb.description = f"You do not have the permissions to {method} {user.name}."
        return emb
                
    @commands.command()
    async def clearreactions(self, ctx, message: int):
        """clear all reactions on a message
        Parameters
        • message - the number of the message from which to remove the reactions
        """
        for i, m in enumerate(await ctx.channel.history(limit = 100).flatten()):
            if i == message:
                await m.clear_reactions()
    
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason='Please write a reason'):
        '''Kick someone'''
        try:
            await ctx.guild.kick(member, reason=reason)
        except:
            success = False
        else:
            success = True

        emb = await self.format_mod_embed(ctx, member, success, 'kick')

        await ctx.send(embed=emb)

    @commands.command(aliases = ["banana"])
    async def ban(self, ctx, member: discord.Member, *, reason='Please write a reason!'):
        '''Ban someone'''
        try:
            await ctx.guild.ban(member, reason=reason)
        except:
            success = False
        else:
            success = True

        emb = await self.format_mod_embed(ctx, member, success, 'ban')

        await ctx.send(embed=emb)

    @commands.command()
    async def unban(self, ctx, name_or_id, *, reason=None):
        '''Unban someone'''
        ban = await ctx.get_ban(name_or_id)

        try:
            await ctx.guild.unban(ban.user, reason=reason)
        except:
            success = False
        else:
            success = True

        emb = await self.format_mod_embed(ctx, ban.user, success, 'unban')

        await ctx.send(embed=emb)

    @commands.command(aliases=['prune'])
    async def purge(self, ctx, amount: int, *, ignore_pins = True):
        '''purge a number of messages
        Parameters
        • amount - the amount of messages to purge
        • ignore_pins - pass a truthy value to ignore pinned messages, defaults to True
        '''
        if ignore_pins:
            await ctx.purge(limit = amount+1, check = lambda m : m.pinned == False)
        else:
            await ctx.purge(limit=amount+1)

    @commands.group(aliases = ["c"], invoke_without_command = True)
    async def clean(self, ctx, amount: int = 15, member: discord.Member = None):
        """delete a number of your own or another users messages
        Parameters
        • amount - the amount of messages to delete
        • member - the member whose messages are to be deleted, deletes your own messages if not specified
        """
        deleted = 0
        await ctx.message.delete()
        user = member or ctx.message.author
        async for m in ctx.channel.history(limit = 100):
            if m.author.id == user.id:
                await m.delete()
                deleted += 1
                if deleted == limit:
                    break
                        
    @clean.command(aliases = ["i"])
    async def images(self, ctx, images_to_delete: int = 10):
        """deletes messages containing images
        Parameters
        • images_to_delete - number of images to delete
        """
        deleted = 0
        async for m in ctx.channel.history():
            if m.attachments:
                await m.delete()
                deleted += 1
                if images_to_delete == deleted:
                    break
        await ctx.message.delete()
                
    @clean.command(aliases = ["b"])
    async def bots(self, ctx, messages_to_delete: int = 15):
        """deletes messages sent by bots
        Parameters
        • messages_to_delete - number of messages to delete
        """
        deleted = 0
        async for m in ctx.channel.history(limit = 200):
            if m.author.bot:
                await m.delete()
                deleted += 1
                if deleted == messages_to_delete:
                    break
        await ctx.message.delete()
        
    @clean.command(aliases = ["w"])
    async def word(self, ctx, messages_to_delete = 10, *, words: str):
        """deletes messages containing the specified words
        Parameters
        • words - the words to search for
        • messages_to_delete - number of messages to delete
        """
        deleted = 0
        async for m in ctx.channel.history(limit = 200):
            if words in m.content:
                await m.delete()
                deleted += 1
                if deleted == messagesToDelete:
                    break
        await ctx.message.delete()
        
    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def addrole(self, ctx, member: discord.Member, *, role: discord.Role):
        '''Add a role to someone else
        Parameter
        • member - the name or id of the member
        • role - the name or id of the role'''
        if not role:
            return await ctx.send('That role does not exist.')
        await member.add_roles(role)
        await ctx.send(f'Added: `{role.name}`')


    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def removerole(self, ctx, member: discord.Member, *, role: discord.Role):
        '''Remove a role from someone else
        Parameter
        • member - the name or id of the member
        • role - the name or id of the role'''
        if not role:
            return await ctx.send('That role does not exist.')
        await member.remove_roles(role)
        await ctx.send(f'Removed: `{role.name}`')

def setup(bot):
	bot.add_cog(Mod(bot))
