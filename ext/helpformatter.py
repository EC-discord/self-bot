import discord
from discord.ext.commands import DefaultHelpCommand

class helpformatter(DefaultHelpCommand):  
  def get_ending_note(self):
    return "A bot made by Mirai#4437"
