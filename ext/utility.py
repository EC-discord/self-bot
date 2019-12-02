import json
from discord import Color

def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return {}
        
@classmethod
def black(cls):
    """A factory method that returns a :class:`Colour` with a value of ``0x000000``."""
    return cls(0x000000)

discord.Color.black=black