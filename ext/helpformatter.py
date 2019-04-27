import discord
from discord.ext.commands import DefaultHelpCommand

class helpformatter(DefaultHelpCommand):
  super().__init__(**args)
  
  def get_ending_note():
    return "A bot made by Mirai#4437"
