def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "no way to do this"


print(divide(1,0))
print(divide(1,2))
