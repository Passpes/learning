def currencyconverter(rate,euros):
    dollars=rate*euros
    return dollars

r=input("enter rate: ")
e=input("enter euros: ")
print(currencyconverter(float(r),float(e)))