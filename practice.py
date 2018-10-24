#first assignment
'''print("hello my name is akash ")
a= ("äcad")
b= ("view")
print(a+b)
name= str(input("what is your name?"))
print(name)
age= int(input("what is your age?"))
print(age)
print("let's get started",end=".\n")
s= ("acadview")
course= ("python")
fee= (5000)
print('%s %s %d '%(s,course,fee))
pi= (3.14)
radius= int(input("what is the radius of circle "))
answer= pi*radius*radius
print("area of circle is ", answer)
'''

#date 23 assignment

#1.
'''year=  int(input("year = "))
if year%4==0:
    print("it is a leap year")
else:
    print("it is not a leap year")
'''
#2.
'''length= int(input("length = "))
breadth = int(input("breadth = "))
if length==breadth:
    print("it is a square")
else:
    print("it is a rectangle")
'''
#3.
'''age1= int(input("age of first person= "))
age2= int(input("age of second person= "))
age3= int(input("age of third person= "))
if age1>age2 and age1>age3:
    print("age1 is oldest")
elif(age2>age3):
    print("age2 is oldest")
else:
    print("age3 is oldest")'''

#4.

'''age = int(input("what is your age? = "))
sex = str(input("m of f? = "))
marital_status = str(input("marital status yes or no? = "))
if sex.upper()=="f":
    print("work only in urban areas.")
elif((sex=="m" or sex=="M") and (age>=20 and age<=40)):
    print("he may work in anywhere.")
elif((sex=="m" or sex=="M") and (age>=40 and age<=60)):
    print("he will work in urban areas only.")
else:
    print("error")
'''
#5.

'''print("cost of item is Rs 100/-")
print("Shop will give discount of 10% if the cost of purchased quantity is more than 1000")
quantity = int(input("quantity = "))
price = 100
if(quantity>10):
    amount = ((quantity*price)/100)*10
    print("discount: ",amount)
    print("your bill: ",quantity*price-amount)
else:
    print("your amount is :", quantity*price)'''

#loop

#1

'''a= 0
while a<=9:
    b= int(input("enter the number"))
    a=a+1
print(a)
'''

#2

'''while True:
    print("hello")
'''

#3.

'''list = [ ]
while True:
    number= int(input("type number = "))
    list.append(number)
    if number==0:
        break
    else:
        print(number*number)'''





#4.



#5.

'''for number in range(1,101):
    if number>1:
        for i in range(2,number):
            if(number%i)==0:
                break
        else:
            print(number)
'''




#6.
'''a= []
while True:
    a.append('*')
    print(a)
'''

#7.
