def celtofah(degree):
    if degree < -273.15:
        return("impossible to reach this value")
    else:
        fahren=degree * 9/5 +32
        return fahren

degree=float(input("Please insert the degree in Celsius: "))
print(celtofah(degree))