'''Write a program Python to calculate l.c.m using while loop.'''

def hcf(a,b):
    while(b!=0):
       a,b = b , a % b
    return a

def lcm(a,b):
    lcm=a*b // hcf(a,b)
    print("lcm is: ",lcm)

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
lcm(a,b)
