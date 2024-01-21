import os
import sys
import time
sys.path.append(os.getcwd())
import time
from lib.core.writer import writer
from lib.core.wordlists import wordlist_gen_ascii
from lib.core.logger import logger
import hashlib

def write_wordlist():
    start_time = time.time()
    for word in wordlist_gen_ascii("hello"):
        writer.write_line = True
        writer._write(word)
        elapsed_time = time.time() - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)
        print(f"\rElapsed Time: {minutes} minutes, {seconds} seconds, and {milliseconds} milliseconds", end="", flush=True)
        time.sleep(0.001) 

def write_wordlist_hashed_sha256(output_file=os.getcwd()+"/temp/hashed.txt"):
    start_time = time.time()
    hash_input = "hello"  # Replace with the desired string to be hashed

    with open(output_file, 'w') as file:
        for word in wordlist_gen_ascii(hash_input):
            hashed_word = hashlib.sha256(word.encode()).hexdigest()
            file.write(hashed_word + '\n')

            elapsed_time = time.time() - start_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)
            print(f"\rElapsed Time: {minutes} minutes, {seconds} seconds, and {milliseconds} milliseconds", end="", flush=True)
            time.sleep(0.001)


write_wordlist_hashed_sha256()