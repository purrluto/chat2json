# welcome to my twisted mind
# this is specifically for parsing some chat messages into json format from plaintext
# thanks!

import json
import sys
import os

def main():
    try:
        file = sys.argv[1]
    except IndexError:
        raise Exception("no file provided!")
    
    msg_list = [] # stores all of the messages

    #split file
    try:
        with open(file, "r") as txt:
            rf = txt.read()
            messages = rf.split("\n\n") # get the individual messages
            
            # from here, we need to format the messages themselves to translate into json.
            for m in messages:
                i = 0 # index always starts as 0

                fullmsg = {
                    "newday": False, # this is false by default
                    "name": "",
                    "date": "",
                    "time": "",
                    "msg": ""
                }

                msg_parts = m.split("\n")

                if msg_parts[0][0] == '-':
                    # first formatting func; can split this out into another function tbh
                    fullmsg.update({"newday": True})
                    i += 1 # update i
                
                # all name, date, and time info should be on second line.
                msg_data = msg_parts[i].split(" ")
                i += 1
                content = "\n".join(msg_parts[i:])
                fullmsg.update({"name": msg_data[0], "date": msg_data[1][:-1], "time": msg_data[2], "msg": content})

                # add to full msg dictionary

                msg_list.append(fullmsg)

            # reverse the list since the messages need to be displayed in order.
            msg_list.reverse()
    except FileNotFoundError:
        raise Exception("no file by that name found! check the path!")
    
    # output
    filename = file.split(".")
    with open(filename[0]+".json", 'w') as output:
        json.dump(msg_list, output, indent=2)

if __name__ == "__main__":
    print("entering program!! ^_^")
    main()
    print("exiting program!! ^_^\n" \
    "your file should be in the directory your original file is in~")