def age_calculation(age):
    print(float(age) + 50)


age = input("please insert your age: ")

if int(age) < 120:
    age_calculation(age)
else:
    print("not possible")