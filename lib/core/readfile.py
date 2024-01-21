import os
import sys
sys.path.append(os.getcwd())

def read_file(path):
    with open(path,"r") as file:
            payload = file.read() 
            rows = payload.split("\n") 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows) 
            return sorted_payload.split("\n")
    
