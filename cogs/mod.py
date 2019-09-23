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
    
    @commands.command(aliases = ["rere"])
    async def removereaction(self, ctx, message: int, emoji: discord.Emoji, member: discord.Member):
        for index, m in enumerate(await ctx.channel.history(limit = 100).flatten()):
          if index == message:
            await m.remove_reaction(emoji, member)
                
    @commands.command()
    async def clearreactions(self, ctx, message: int):
        for index, m in enumerate(await ctx.channel.history(limit = 100).flatten()):
            if index == message:
                await m.clear_reactions()
    
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason='Please write a reason!'):
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
    async def purge(self, ctx, limit: int, ignore_pins = None):
        '''Clean a number of messages
        set ignore_pins to p to ignore pinned messages
        e.g (prefix)purge 30 p'''
        if ignore_pins == "p":
            await ctx.purge(limit = limit + 1, check = lambda m : m.pinned == False)
        else:
            await ctx.purge(limit=limit+1)

    @commands.group(aliases = ["c"], invoke_without_command = True)
    async def clean(self, ctx, limit: int = 15, member: discord.Member = None):
        """delete a number of your own or another users messages
        Parameters
        • limit - number of messages to delete
        • member - the name or id of the member whose messages are to be deleted
        """
        deleted = 0
        user = member or ctx.message.author
        async for m in ctx.channel.history(limit = 100):
            if m.author.id == user.id:
                await m.delete()
                deleted += 1
                if deleted == limit:
                    break
                        
    @clean.command(aliases = ["i"])
    async def images(self, ctx, imagesToDelete: int = 10):
        """deletes messages containing images
        Parameters
        • imagesToDelete - number of images to delete
        """
        deleted = 0
        async for m in ctx.channel.history():
            if m.attachments:
                await m.delete()
                deleted += 1
                if imagesToDelete == deleted:
                    break
        await ctx.message.delete()
                
    @clean.commands(aliases = ["b"])
    async def bots(self, ctx, messagesToDelete: int = 15):
        """deletes messages sent by bots
        Parameters
        • messagesToDelete - number of messages to delete
        """
        deleted = 0
        async for m in ctx.channel.history(limit = 200):
            if m.author.bot:
                await m.delete()
                deleted += 1
                if deleted == messagesToDelete:
                    break
        await ctx.message.delete()

    @commands.command()
    async def baninfo(self, ctx, *, name_or_id):
        '''Check the reason of a ban from the audit logs.'''
        ban = await ctx.get_ban(name_or_id)
        em = discord.Embed()
        em.color = await ctx.get_dominant_color(ban.user.avatar_url)
        em.set_author(name=str(ban.user), icon_url=ban.user.avatar_url)
        em.add_field(name='Reason', value=ban.reason or 'None')
        em.set_thumbnail(url=ban.user.avatar_url)
        em.set_footer(text=f'User ID: {ban.user.id}')

        await ctx.send(embed=em)

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def addrole(self, ctx, member: discord.Member, *, role: discord.Role):
        '''Add a role to someone else.'''
        if not role:
            return await ctx.send('That role does not exist.')
        await member.add_roles(role)
        await ctx.send(f'Added: `{role.name}`')


    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def removerole(self, ctx, member: discord.Member, *, role: discord.Role):
        '''Remove a role from someone else.'''
        if not role:
            return await ctx.send('That role does not exist.')
        await member.remove_roles(role)
        await ctx.send(f'Removed: `{role.name}`')

def setup(bot):
	bot.add_cog(Mod(bot))
