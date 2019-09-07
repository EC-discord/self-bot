import discord
from discord.ext.commands import DefaultHelpCommand

class helpformatter(DefaultHelpCommand):
  def __init__(self, bot):
    self.bot = bot
    
  def get_ending_note(self):
    return f"A bot made by {self.bot.application_info().owner}"
