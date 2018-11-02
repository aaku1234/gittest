#1.
'''a= []
b= input("enter the list ")
a.append(b)
a.append("google,apple,facebook,microsoft,tesla")
print(a)
'''


#2.
'''a= ["a","c","d","e","g","a","d","c","s"]
print(a.count("a"))
'''

#3.
'''asc= [2,234,4,343,254,465,67,456,45]
a= sorted(asc)
print(a)
'''

#4.
'''a = [2,5,3,45,456,23,545,65]
b = [56,43,563,534,67,12,11]
c= sorted(a)
d = sorted(b)
e= []
e.extend(c)
e.extend(d)
f= sorted(e)
print(f)
for i in f:
    if(i%2==0):
        print("it is even")
    else:
        print("it is odd")
'''


#TUPLES
#1.
'''a= (1,5,43,2342,4543,234,65,9)
print(a[::-1])
print(max(a))
print(min(a))
'''

#STRINGS
#1.
'''name=("my name is akash")
print(name.upper())
print(type(name))
if(name==int):
    print("true")
else:
    print("false")

'''

#2.
'''a= ("hello world")
b= a.replace("world","akash")
print(b)

'''




























