import os
import sys
sys.path.append(os.getcwd())
from lib.core.readfile import read_file
import hashlib
#!hashed wordlist from server
#! generated wordlist 

import hashlib

def match_wordlist(hashed_wordlist_from_server="/Users/alimirmohammad/pycrack-ng/testwordlistfromserver.txt", my_wordlist="/Users/alimirmohammad/pycrack-ng/temp/captures.txt"):
    wordlist = read_file(my_wordlist=my_wordlist)
    #! this is generated wordlist
    with open(hashed_wordlist_from_server, 'r') as file: 
        #! This is the hashed wordlist file from the server received
        hashes = file.read().splitlines()

    for word in wordlist:
        for hashed_word in hashes:
            if hashlib.sha256(word.encode()).hexdigest() == hashed_word:
                print(f"Match found: Plain Text: {word}, Hash: {hashed_word}")
                raise SystemExit
        else:
            print(f"No match found for: {word}")

def read_file(my_wordlist):
    with open(my_wordlist, 'r') as file:
        return file.read().splitlines()

# Example usage
# match_wordlist()


