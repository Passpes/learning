import json
from difflib import get_close_matches

data = json.load(open("data.json"))
i = 1

def translate(w):
    if w.istitle():
        w = w
    else:    
        w = w.lower()
        
    if w in data:
        return data[w]
    elif len (get_close_matches(w,data.keys())) > 0:
        yn = input("We suggest the word %s instead, Enter Y if yes, or N if no: " % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        else:
            exit()
    else:
        return "the word u are searching for doesn't exist!"

word = input("Which word are u looking for: ")

output = (translate(word))

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)