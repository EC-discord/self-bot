import discord
from discord.ext.commands import DefaultHelpCommand
from discord.ext.commands import bot

class helpformatter(DefaultHelpCommand):
  def get_ending_note(self):
    return f"A bot made by {bot.user}"
