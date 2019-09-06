import discord
from discord.ext.commands import DefaultHelpCommand

class helpformatter(DefaultHelpCommand):  
  def get_ending_note(self):
    return f"A bot made by {bot.application_info().owner}"
