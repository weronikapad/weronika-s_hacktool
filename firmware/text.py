import os
from main1 import filename

def run(show, get_input):
    
    while True:
        text = get_input()
        with open(filename, 'a') as f:
            f.write(text)
        if text == "esc":
            with open(filename, 'a') as f:
                f.close()
            return 
    
    
