####################syntax#######
#print ("hi there")
var1 = 3
#print (myvar)
var1 += 2
#myvar
str1 = "Hi"
#print (var1)
str1 += " bliCrigtz"
#print (str1)
str1,var1 = var1,str1
#print (str1,var1)
############################data types################
########Lists example######
sample = [1, ["another","list"],("a3","getzlib")]
mylist = ["list item 1",2,3.14]
#print (mylist[::2])
#print (mylist[:])
#print (mylist[-2])
#print (sample[2])

########dict example#####
mydict = {"key 1": "35694:2598", 2: 3, "pi": 3.14}
#print(mydict[])
#print (mydict["key 1"])
#print (mydict [2])

#######tuple example#######
mytup = (2658,485,3417,586,5687)
#print (mytup[2])

#####function####
func1 = len
#print(len(mytup))

####################strings##########
str2 = " blitz"
#print("Name: %s \nNumber: %s\nString: %s" %(str2, 3, 3 * "-"))
vmm = (125,126,127,128,129)
lv = ["CentOs 7.3", "Debian", "Ubuntu1 6.04", "Gentoo"]
users =("flex","radi","lpico","brew")
ip=("10.9.80.100" ,"10.9.80.101")
#print ("VM number: %(vmn)s \nLinux version %(lv)s \nUsers %(users)s \nIp address %(ip)s" % {"vmn":vmm[1], "lv":lv[1], "users":users[:2], "ip":ip[1] })

#####################flow control statements#############

rangelist = range(10)
#print(rangelist)
# for n in rangelist:
#     if n in (4, 6, 5, 8):
#         print (n)
#         break
#     else:
#         print ("n not listed")
#     break

# if rangelist[1] == 2:
#     print("the second item is 2")
# elif rangelist[1] == 3:
#     print("the second item is 3")
# else:
#     print("Dunno")

######################functions########################

funcvar = lambda x: x +1
#print(funcvar(1))

def pass1(lv, an_int=2, a_string=" connecting to host for deployment"):
    lv.append("Ubuntu 12.04")
    an_int = 6
    return lv, an_int, a_string

# print(pass1(lv, var1))
# print(lv, var1)

###########################classes###################
class M1(object):
    common = 10
    def __init__(self):
        self.myvar = ip[1]
    def myfn1(self, arg1, arg2):
        return self.myvar, arg1, arg2

classinstance1 = M1()
#print(classinstance1.myfn1(lv[1], users[:3]))

classinstance2 = M1()
#print(classinstance2.common)

classinstance1.common = 30
#print(classinstance1.common)
#print(classinstance2.common)

M1.common = 15

#print(classinstance1.common)
#print(classinstance2.common)

class ClassA(M1):
    def __init__(self, arg1):
        self.myvar = 3
        # print(arg1)

classinstance1= ClassA("hi")
#print(classinstance1)

#print(classinstance1.myfn1(1,2))

classinstance1.test =15
#print(classinstance1.test)

#############################Exception###############
def some_func():
    try:
        10/0
    except ZeroDivisionError:
        print("Invalid.")
    else:
        pass
    finally:
        print("We're done")

#some_func()

###################importing########################
import random
#from time import clock
randomint = random.randint(1,100)
#print(randomint)

#####################file I/O ###################


import pickle
mylist = ["This", "is", 4, 13327]
mylista = []
myfile1 = open(r"C:binary.dat", "wb")
pickle.dump(mylista, myfile1)
#print(mylista)
myfile1.close()

myfile = open (r"C:text.txt","w")
myfile.write("text to dump in the file")
myfile.close()

myfile = open(r"C:text.txt")
#print(myfile.read())
myfile.close()

myfile1 = open("C:binary.dat", "rb")
loadedlist = pickle.load(myfile1)
#print(myfile)
#myfile.close()
print(loadedlist) 

###Miscellaneous
lst1 = [1,2,3]
lst2 = [3,4,5]
lst3 = [3,3,4,4,3]

# print([x * y for x in lst1 for y in lst2])
#print([x for x in lst1 for y in lst2 if 5 > y > 1 ])

#print (any([i % 3 for i in [3,3,4,3]]))
del lst3[2]

#print (sum(2.5 for i in lst3 if i == 4))

number = 5

def myfunc():
    print(number)

def anotherfunc():
    number = 3
    print(number)
    

def yetanotherfunc():
    global number
    print(number)
    number = 3

#myfunc()
#anotherfunc() 
#yetanotherfunc()   

vm = (125,126,127,128,129)

# for i in lv:
#     print(i)

# def hi_python():
#     print("hi python!")
# hi_python()

# from appkit import NSScreen
# width = NSScreen.mainScreen().frame().size.width
# height = NSScreen.mainScreen().frame().size.height

# print(width, height)
