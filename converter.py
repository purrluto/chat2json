# welcome to my twisted mind
# this is specifically for parsing some chat messages into json format from plaintext
# thanks!

import json
import sys

def main():
    print("entering the program, ok?")

    try:
        file = sys.argv[1]
    except IndexError:
        raise Exception("No file provided.")
    
    #split file
    with open(file) as txt:
        rf = txt.read()
        messages = rf.split("\n\n")
    
    # output
    filename = file.split(".")
    print(filename)
    with open(filename[0]+".json", 'w') as output:
        output.writelines(str(messages))

if __name__ == "__main__":
    main()