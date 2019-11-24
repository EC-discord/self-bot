import discord
from discord.ext import commands
from discord.ext.commands import DefaultHelpCommand
from discord.ext.commands import bot

class helpformatter(DefaultHelpCommand, commands.Cog):
  def get_ending_note(self, ctx):
    return f"A bot made by {ctx.bot.user}"
