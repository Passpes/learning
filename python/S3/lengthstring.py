def lengthstring(string):
    if type(string) == int or type(string) == float:
        return "Sorry integers don't have length"
    else:
        return len(string)

string = input("what's your string  ")

print(lengthstring(string))