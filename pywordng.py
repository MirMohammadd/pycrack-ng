from lib.core.writewordlist import write_wordlist,write_wordlist_hashed_sha256

def main():
    hash_or_not = input("enter 1 for generating the plaintext wordlist and 2 for hashed wordlist:")
    if hash_or_not == "1":
        _wrd = input("enter most possible word for generating combination:")
        write_wordlist(words=_wrd)
    elif hash_or_not == "2":
        _wrds = input("enter the possible word for generating the hashes.")
        write_wordlist_hashed_sha256(hash_input=_wrds)  

if __name__ == "__main__":
        try:
            main()  
        
        except Exception as e:
            print(e)