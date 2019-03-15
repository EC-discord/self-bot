
# -*- coding: utf-8 -*-

"""
The MIT License (MIT)
Copyright (c) 2015-2017 Rapptz
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import itertools
import inspect
import asyncio
import discord
from discord.ext import commands
from discord.ext.commands.core import GroupMixin, Command
from discord.ext.commands.errors import CommandError


class Paginator:
    """A class that aids in paginating embeds for Discord messages.
    Attributes
    -----------
    max_size: int
        The maximum amount of codepoints allowed in a page.
    """
    def __init__(self, max_size=1995):
        self.max_size = max_size
        self._current_embed = discord.Embed()
        self._current_field = []
        self._count = 0
        self._embeds = []
        self.last_cog = None

    def add_line(self, line='', *, empty=False):
        """Adds a line to the current embed page.
        If the line exceeds the :attr:`max_size` then an exception
        is raised.
        Parameters
        -----------
        line: str
            The line to add.
        empty: bool
            Indicates if another empty line should be added.
        Raises
        ------
        RuntimeError
            The line was too big for the current :attr:`max_size`.
        """
        if len(line) > self.max_size - 2:
            raise RuntimeError('Line exceeds maximum page size %s' % (self.max_size - 2))

        if self._count + len(line) + 1 > self.max_size:
            self.close_page()

        self._count += len(line) + 1
        self._current_field.append(line)

        if empty:
            self._current_field.append('')

    def close_page(self):
        """Prematurely terminate a page."""
        name = value = ''
        while self._current_field: 
            curr = self._current_field.pop(0) # goes through each line
            if curr.strip().endswith(':'): # this means its a CogName:
                if name: 
                    if value:
                        self._current_embed.add_field(name=name, value=value)
                        name, value = curr, '' # keeps track of the last cog sent,
                        self.last_cog = curr  # so the next embed can have a `continued` thing                      
                else:                          
                    if value:
                        if self.last_cog:
                            self._current_embed.add_field(name=f'{self.last_cog} (continued)', value=value)
                        value = ''
                    name = curr
                    self.last_cog = curr
            else:
                value += curr + '\n'

        # adds the last parts not done in the while loop
        print(self.last_cog)
        if self.last_cog and value:
            self._current_embed.add_field(name=self.last_cog, value=value)
            value = ''

        # this means that there was no `Cog:` title thingys, that means that its a command help
        if value and not self.last_cog:
            fmt = list(filter(None, value.split('\n')))
            self._current_embed.title = f'``{fmt[0]}``' # command signiture
            self._current_embed.description = '\n'.join(fmt[1:]) # command desc

        self._embeds.append(self._current_embed)
        self._current_embed = discord.Embed()
        self._current_field = []
        self._count = 1

    @property
    def pages(self):
        """Returns the rendered list of pages."""
        # we have more than just the prefix in our current page
        if len(self._current_field) > 1:
            self.close_page()
        return self._embeds 

    def __repr__(self):
        fmt = '<Paginator max_size: {0.max_size} count: {0._count}>'
        return fmt.format(self)        
