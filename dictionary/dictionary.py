import json
from difflib import get_close_matches
data=json.load(open("original.json"))
def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.upper()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("Did you mean %s instead" %get_close_matches(word,data.keys())[0])
        decide=input("press y for yes or n for no")
        if decide=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide=="n":
            return ("wrong keys entered")
        else:
            return ("You have entered wrong input please enter just y or n")
    else:
        return ("wrong keys entered")
word=input("Enter the word you want to search")
output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
