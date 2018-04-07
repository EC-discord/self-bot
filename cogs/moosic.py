import discord
from discord.ext import commands
import random

class moosic:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def playmusic(self, ctx, prefix):
        music = ['avicii the nights audio', 'zhiend blood color', 'imagine dragons demons audio', 'chainsmokers closer lyrics'
        , 'tokyo ghoul op unravel', 'layers recreators', 'imagine dragons bleeding out', 'akame ga kill op 1'
        , 'onerepublic kids audio', 'starset it has begun']
        song = random.choice(music)
        while True:
            await ctx.send(f'{prefix}play {song}')
            music.remove(song)
            await asyncio.sleep(240)
            if ctx.message.content = '*break!':
                break

def setup(bot):
    bot.add_cog(moosic(bot))
