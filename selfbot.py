import discord
from discord.ext import commands
from ext.context import CustomContext
from ext.formatter import EmbedHelp
from ext import embedtobox
import asyncio
import aiohttp
import datetime
import psutil
import time
import json
import sys
import os
import re
import textwrap
from PIL import Image

class Selfbot(commands.Bot):
    '''
    Custom Client for selfbot.py - Made by someone
    '''
    _mentions_transforms = {
        '@everyone': '@\u200beveryone',
        '@here': '@\u200bhere'
    }

    _mention_pattern = re.compile('|'.join(_mentions_transforms.keys()))

    def __init__(self, **attrs):
        super().__init__(command_prefix=self.get_pre, self_bot=True)
        self.formatter = EmbedHelp()
        self.session = aiohttp.ClientSession(loop=self.loop)
        self.process = psutil.Process()
        self._extensions = [x.replace('.py', '') for x in os.listdir('cogs') if x.endswith('.py')]
        self.remove_command('help')
        self.load_extensions()
        

    def load_extensions(self, cogs=None, path='cogs.'):
        '''Loads the default set of extensions or a seperate one if given'''
        for extension in cogs or self._extensions:
            try:
                self.load_extension(f'{path}{extension}')
                print(f'Loaded extension: {extension}')
            except Exception as e:
                print(f'LoadError: {extension}\n'
                      f'{type(e).__name__}: {e}')

   
    @property
    def token(self):
        '''Returns your token wherever it is'''
        with open('data/config.json') as f:
            config = json.load(f)
            if config.get('TOKEN') == "your_token_here":
                if not os.environ.get('TOKEN'):
                    self.run_wizard()
            else:
                token = config.get('TOKEN').strip('\"')
        return os.environ.get('TOKEN') or token

    @staticmethod
    async def get_pre(bot, message):
        '''Returns the prefix.'''
        with open('data/config.json') as f:
            prefix = json.load(f).get('PREFIX')
        return os.environ.get('PREFIX') or prefix or 'r.'

    def restart(self):
        os.execv(sys.executable, ['python'] + sys.argv)

    @staticmethod
    def run_wizard():
        '''Wizard for first start'''
        print('------------------------------------------')
        token = input('Enter your token:\n> ')
        print('------------------------------------------')
        prefix = input('Enter a prefix for your selfbot:\n> ')
        data = {
                "TOKEN" : token,
                "PREFIX" : prefix,
            }
        with open('data/config.json','w') as f:
            f.write(json.dumps(data, indent=4))
        print('------------------------------------------')
        print('Restarting...')
        print('------------------------------------------')
        os.execv(sys.executable, ['python'] + sys.argv)

    @classmethod
    def init(bot, token=None):
        '''Starts the actual bot'''
        selfbot = bot()
        safe_token = token or selfbot.token.strip('\"')
        try:
            selfbot.run(safe_token, bot=False, reconnect=True)
        except Exception as e:
            print(e)

    async def on_connect(self):
        print('---------------\n'
              'selfbot.py connected!')

    async def on_ready(self):
        '''Bot startup, sets uptime.'''
        if not hasattr(self, 'uptime'):
            self.uptime = datetime.datetime.utcnow()
        print(textwrap.dedent('Logged in!'))

    async def process_commands(self, message):
        '''Utilises the CustomContext subclass of discord.Context'''
        ctx = await self.get_context(message, cls=CustomContext)
        if ctx.command is None:
            return
        await self.invoke(ctx)
    
    async def on_member_update(self, before, after):
        stats = {"online" : discord.Status.online, "dnd" : discord.Status.dnd, "idle" : discord.Status.idle, "invisible" : discord.Status.invisible}
        if after.status != before.status:
            await self.bot.change_presence(status = stats[after.status])

if __name__ == '__main__':
    Selfbot.init()
