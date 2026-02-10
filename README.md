# pluto purrluto's chat2json python script

this is my handy-dandy chatlog message parser since i really didn't want to do all of that by hand

## formatting
this is meant to basically take chat msg rp things and convert it into json.. the format goes like this:

```
- YYYY-MM-DD -
NAME YYYY-MM-DDD, HH:MM
message content (as long as you want)

NAME YYYY-MM-DDD, HH:MM
message content (as long as you want)

...

NAME YYYY-MM-DDD, HH:MM
message content (as long as you want)
```

the - YYYY-MM-DD - is used to figure out if it's a new day for the json

this converts it into this json format:
```json
"newday": true/false,
"name": "NAME",
"date": "YYYY-MM-DD",
"time": "HH:MM"
"msg": "message content (as long as you want)"
```

it doesn't work with other ones but it's nice for #me

## inputs and outputs
you put in a formatted txt file (can be absolute filepath i believe)
you get out a json file
wow!

## running the thing
this is on python 3.10.12!
to run the command, just do:

> python3 chat2json.py filename.txt
or
> python chat2json.py filename.txt

however with the above you do have to have the absolute filepath and run it in the project folder...

if you wanna get real fancy with it, u can add it to the environment variables so u can just do
> chat2json filename.txt
from the directories you have your file in!! handy!

### todo

this part isn't important but i might expand this later. would be nice to have something that fixes the json formats for everything.
also need to add in erroring for invalid filenames
will also add in a tutorial for adding it to the path in windows b/c i think that makes it easier to use

finally, maybe i'll do a bulk convert at some point and add some like argument explanation things, idk