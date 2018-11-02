#1.
'''radius = int(input("ënter the radius of sphere "))
def sphere(radius):
    sphere = 4*3.14*radius*radius
    return sphere
print("area: ",sphere(radius))'''

#2.
'''i = int(input("enter the number "))
for num in range(1,11):
    a= i*num
    print(i,"*",num,"=",a)'''

#3.
'''a= int(input("enter the number"))
b= int(input("enter the 2nd number"))
def power(a,b):
    if(b==1):
        return a
    else:
        return a*power(a,b-1)

print("factorial of number is: ",power(a,b))'''

#4.
'''n= int(input("enter the number: "))
sum1=0
for i in range(1,n):
    if(n%i==0):
        sum1= sum1+i
if(sum1==n):
    print("the number is a perfect number")
else:
    print("the number is not a perfect number")'''
