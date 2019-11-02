import discord
from discord.ext import commands
from ext.context import CustomContext
from ext.helpformatter import helpformatter
from ext import embedtobox
import aiohttp
import json
import os
import re
import traceback
    
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
        super().__init__(command_prefix=self.get_pre, self_bot=True, help_command = helpformatter(), guild_subscriptions = False)
        self.session = aiohttp.ClientSession(loop=self.loop)
        self.load_extensions()

    def load_extensions(self):
        for extension in ["cogs.anim", "cogs.misc", "cogs.mod", "cogs.noble", "cogs.skid", "cogs.source", "cogs.textemotes", "cogs.utils"]:
            try:
                self.load_extension(extension)
                print(f'Loaded extension: {extension[5:]}')
            except:
                print(f'LoadError: {extension[5:]}\n'
                      f'{traceback.print_exc()}')

   
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
        print('---------------')
        print('connected!')

    async def on_ready(self):
        '''Bot startup'''
        print('Logged in!')

    async def process_commands(self, message):
        '''Utilises the CustomContext subclass of discord.Context'''
        ctx = await self.get_context(message, cls=CustomContext)
        self.ctx = await self.get_context(message, cls=CustomContext)
        if ctx.command is None:
            return
        await self.invoke(ctx)
    
    async def on_message_edit(self, before, after):
        await self.process_commands(after)
    
    async def on_message(self, message):
        r = re.compile(r">(#\d{6}) (.*)")
        r = r.match(message.content)
        if r.group():
            await m.delete()
            await ctx.send(embed = discord.Embed(color = discord.Color(f"{r.group(1)}"), description = r.group(2))
        await self.process_commands(message)
                           
if __name__ == '__main__':
    Selfbot.init()
