from discord.ext import commands


class textemotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def thumbs(self, ctx):
        """(👍' - ')👍"""
        await ctx.message.edit(content="(👍' - ')👍")

    @commands.command()
    async def cookie(self, ctx):
        """(  ' - ')-🍪"""
        await ctx.message.edit(content="(  ' - ')-🍪")

    @commands.command()
    async def cat(self, ctx):
        await ctx.message.edit(content=r"""{ \  / }
( ^ - ^ )
( u   u )～""")

    @commands.command()
    async def pew(self, ctx):
        """(   ' - ')>---------- pew pew"""
        await ctx.message.edit(content="(   ' - ')>---------- pew pew")

    @commands.command()
    async def lpew(self, ctx):
        """pew pew ----------<(' - '   )"""
        await ctx.message.edit(content="pew pew ----------<(' - '   )")


def setup(bot):
    bot.add_cog(textemotes(bot))
