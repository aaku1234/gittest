#1.
d={}
x= input("enter the key: ")
    
print(x)

y = input("enter the value: ")
print(y)   
d[x]=y
    
print(d)


#2.

students= {'arun': {'maths':85,'bio':90},'surya':{'maths':90,'bio': 85}}
print("enter the name of the student 1.arun  2.surya")
name= input("name of the student ")
print("enter the subject of the student 1.maths  2.bio ")
subject= input("name of subject ")
print(students[name][subject])
