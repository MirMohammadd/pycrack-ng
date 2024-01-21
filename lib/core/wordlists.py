import os
import sys
from itertools import product
import string

sys.path.append(os.getcwd())

import lib.core.settings as settings
from lib.core.logger import logger

def wordlist_gen_ascii(keyword):
    all_characters = settings.ALL+ string.digits + string.punctuation

    for combination in product(all_characters, repeat=len(keyword)):
        yield ''.join(map(str, combination))
        yield keyword + ''.join(map(str, combination))
        yield ''.join(map(str, combination)) + keyword

# wordl = wordlist_gen_ascii("hello")

# for word in wordl:
#     print(word)
