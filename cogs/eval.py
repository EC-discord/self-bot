import datetime
import discord
from discord.ext import commands
from utils import coliru


LANGUAGE_IMAGES = {
    'c':     'https://cdn.discordapp.com/emojis/232956938965614592.png',
    'cpp':   ('http://logos-vector.com/images/logo/xxl/'
              '1/3/7/137285/C__7d201_450x450.png'),
    'py':    ('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/'
              'Python-logo-notext.svg/1024px-Python-logo-notext.svg.png'),
    'sh':    ('https://openforums.files.wordpress.com/'
              '2013/06/terminal-icon-512x512.png'),
    'ruby':  ('https://cdn.codementor.io/assets/topic/category_header/'
              'ruby-on-rails-bc9ab2af8d92eb4e7eb3211d548a09ad.png'),
    'lua':   ('https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/'
              'Lua-Logo.svg/947px-Lua-Logo.svg.png'),
    'perl':  ('https://engineering.purdue.edu/people/joseph.r.kline.1/talks/'
              'ppw/images_to_use/perl-onion-logo.png'),
    'perl6': 'https://hbfs.files.wordpress.com/2009/11/camelia-logo.png'
}

LANGUAGE_NAMES = {
    'c':     'C',
    'cpp':   'C++',
    'py':    'Python',
    'sh':    'Shell',
    'ruby':  'Ruby',
    'lua':   'Lua',
    'perl':  'Perl',
    'perl6': 'Perl 6'
}


class Eval:
    """Evaluation Command(s) using the Coliru API."""

    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def get_lang(code_block: str) -> str:
        """Returns the language specified for the markup of a codeblock."""

        to_newline = code_block[3:code_block.find('\n')]
        return to_newline.replace(' ', '').replace('\n', '')

    @commands.command(name='evaluate')
    async def eval_(self, ctx, *, code_block: str):
        """Evaluate the given Codeblock. The language must be specified."""
        lang = self.get_lang(code_block)
        if lang not in coliru.LANGS:
            await ctx.send(embed=discord.Embed(
                title='Eval: Unknown Language',
                description=f'Known languages: {", ".join(coliru.LANGS)}',
                colour=discord.Colour.red()
            ))
        else:
            code = code_block.strip('`')[len(lang):]
            start_time = datetime.datetime.now()
            result = await coliru.evaluate(lang, code)
            execution_time = datetime.datetime.now() - start_time
            await ctx.send(embed=discord.Embed(
                colour=discord.Colour.blue()
            ).add_field(
                name='Eval Results',
                value=f'```{lang}\n{result}```'
            ).set_author(
                name=ctx.message.author,
                icon_url=ctx.message.author.avatar_url
            ).set_footer(
                text=(f'{LANGUAGE_NAMES[lang]} Evaluation |'
                      f' Execution time: {str(execution_time)[:-4]}'),
                icon_url=LANGUAGE_IMAGES[lang]
            ))


def setup(bot):
    bot.add_cog(Eval(bot))
