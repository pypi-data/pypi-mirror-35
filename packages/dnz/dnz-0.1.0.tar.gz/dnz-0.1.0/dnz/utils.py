import re
import random
import subprocess
import platform
from typing import Any


def is_valid_hostname(hostname: str) -> bool:
    """
    Checks whether hostname is a valid hostname
    Adapted from https://stackoverflow.com/questions/2894902/check-for-a-valid-domain-name-in-a-string/2894922

    Args:
        hostname: Hostname (e.g. python.org)

    Returns:
        bool: True for valid, False otherwise.

    """
    valid_domain_re = r'^(?=.{1,253}$)(?!.*\.\..*)(?!\..*)([a-zA-Z0-9-]{,63}\.){,127}[a-zA-Z0-9-\.]{1,63}$'
    return re.match(valid_domain_re, hostname) is not None


def ping(hostname: str):
    """
    Perform network ping to host

    Args:
        hostname: Hostname (e.g. python.org)

    Returns:
        bool: True if ping is successful, false otherwise.

    """

    args = '-n 1' if platform.system().lower() == 'windows' else '-c 1'
    cmd = f'ping {args} {hostname}'
    need_sh = False if platform.system().lower() == 'windows' else True

    return subprocess.call(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT,
                           shell=need_sh) == 0


def generate_name(delimiter: str = '-', token_chars: str = '0123456789', token_len: int = 6):
    """
    Generate unique names based on nouns, adjectives, and number tokens
    e.g.: round-bread-144151

    Adapted from https://github.com/Atrox/haikunatorpy

    Args:
        delimiter: Delimiter to demarcate adjectives and nouns
        token_chars: Characters to use for unique token at end of name
        token_len: Length of unique token at end of name

    Returns:
        name
    """

    adjectives = [
        'aged', 'ancient', 'autumn', 'billowing', 'bitter', 'black', 'blue', 'bold',
        'broad', 'broken', 'calm', 'cold', 'cool', 'crimson', 'curly', 'damp',
        'dark', 'dawn', 'delicate', 'divine', 'dry', 'empty', 'falling', 'fancy',
        'flat', 'floral', 'fragrant', 'frosty', 'gentle', 'green', 'hidden', 'holy',
        'icy', 'jolly', 'late', 'lingering', 'little', 'lively', 'long', 'lucky',
        'misty', 'morning', 'muddy', 'mute', 'nameless', 'noisy', 'odd', 'old',
        'orange', 'patient', 'plain', 'polished', 'proud', 'purple', 'quiet', 'rapid',
        'raspy', 'red', 'restless', 'rough', 'round', 'royal', 'shiny', 'shrill',
        'shy', 'silent', 'small', 'snowy', 'soft', 'solitary', 'sparkling', 'spring',
        'square', 'steep', 'still', 'summer', 'super', 'sweet', 'throbbing', 'tight',
        'tiny', 'twilight', 'wandering', 'weathered', 'white', 'wild', 'winter', 'wispy',
        'withered', 'yellow', 'young'
    ]

    nouns = [
        'art', 'band', 'bar', 'base', 'bird', 'block', 'boat', 'bonus',
        'bread', 'breeze', 'brook', 'bush', 'butterfly', 'cake', 'cell', 'cherry',
        'cloud', 'credit', 'darkness', 'dawn', 'dew', 'disk', 'dream', 'dust',
        'feather', 'field', 'fire', 'firefly', 'flower', 'fog', 'forest', 'frog',
        'frost', 'glade', 'glitter', 'grass', 'hall', 'hat', 'haze', 'heart',
        'hill', 'king', 'lab', 'lake', 'leaf', 'limit', 'math', 'meadow',
        'mode', 'moon', 'morning', 'mountain', 'mouse', 'mud', 'night', 'paper',
        'pine', 'poetry', 'pond', 'queen', 'rain', 'recipe', 'resonance', 'rice',
        'river', 'salad', 'scene', 'sea', 'shadow', 'shape', 'silence', 'sky',
        'smoke', 'snow', 'snowflake', 'sound', 'star', 'sun', 'sun', 'sunset',
        'surf', 'term', 'thunder', 'tooth', 'tree', 'truth', 'union', 'unit',
        'violet', 'voice', 'water', 'waterfall', 'wave', 'wildflower', 'wind', 'wood'
    ]


    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    token = ''.join(random.choice(token_chars) for _ in range(token_len))

    sections = [adjective, noun, token]
    return delimiter.join(filter(None, sections))
