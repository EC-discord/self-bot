import json

import aiohttp

LANGS = {
    'c':     'mv main.cpp main.c && gcc -std=c11 -Wall -Wextra -pthread main.c && ./a.out',
    'cpp':   'g++ -std=c++1z -Wall -Wextra -pthread main.cpp && ./a.out',
    'sh':    'sh main.cpp',
    'py':    'python3 main.cpp',
    'ruby':  'ruby main.cpp',
    'lua':   'lua main.cpp',
    'perl':  'perl main.cpp',
    'perl6': 'perl6 main.cpp'
}


async def post(cmd: str, src: str):
    """
    Sends a POST request to the Coliru API
    with the specified compilation command
    and the given source code. Returns the result.
    """

    data = json.dumps({'cmd': cmd, 'src': src})
    async with aiohttp.ClientSession() as cs:  # pylint: disable=invalid-name
        async with cs.post('http://coliru.stacked-crooked.com/compile', data=data) as res:
            return await res.text()


async def evaluate(lang: str, src: str):
    """
    Evaluate Code using the Coliru API.
    `lang` is the syntax highlighter that was used -
    see the dictionary LANGS' keys.
    `src` is the source code that should be evaluated.
    Note that
        - C is compiled with the C 11 standard
        - C++ is compiled with the C++ 17 standard
        - Python is always Python 3
    """

    lang_cmd = LANGS.get(lang, None)
    if lang_cmd is None:
        return None
    return await post(lang_cmd, src)
