'''Write a program in Python to calculate H.C.F using while loop.'''

def hcf(a,b):
    while(b!=0):
       a,b = b,a % b
    return a

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(hcf(a,b))