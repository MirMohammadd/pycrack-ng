import os
import sys
sys.path.append(os.getcwd())

import lib.core.settings as settings
from lib.core.logger import logger

def wordlist_gen_ascii(keyword:str,upper=False,lower=False,digit=False,adv=False):
    if upper:
        for word in settings.UPPER_LETTERS:
            yield keyword + word
            yield word + keyword
            if adv:
                yield word + "".join(keyword)
        
        logger.debug(settings.WORDLIST_GENERATED_MSG%__file__)
        return
    
    elif lower:
        for word in settings.LOWER_LETTERS:
            yield keyword + word
            yield word + keyword
            if adv:
                yield word + "".join(keyword)
                
        logger.debug(settings.WORDLIST_GENERATED_MSG%__file__)
        return
    
    elif digit:
        for idx,word in enumerate(settings.DIGITS):
            for num1 in settings.DIGITS:
                for num2 in settings.DIGITS:
                    if num1 == num2:
                        continue
                    _ = 0
                    idx += len(word) if word == 0 else idx
                    yield keyword + str(word)+str(idx)
                    yield str(word)+str(idx) + keyword
                    if adv:
                        yield str(word)+str(idx) + "".join(keyword)
                        yield keyword.replace(keyword[len(keyword)-1])
                        yield str(word)+keyword+str(word)+""
                
        logger.debug(settings.WORDLIST_GENERATED_MSG%__file__)
        return
    

wordl = wordlist_gen_ascii("hello",digit=True)
for word in wordl:
    print(word)
            