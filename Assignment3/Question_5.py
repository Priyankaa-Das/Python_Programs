''' Write a program to print out all Armstrong numbers between 1 and 500. 
    If sum of cubes of each digit of the number is equal to the number itself, 
    then the number is called an Armstrong number For example. 153 (111)-(555)-(3*3*3)'''
    
num=int(input("Enter a number:"))
sum=0
for i in range(1,500):
    n=i
    temp=n
    while n>0:
        digit=n%10
        sum=sum + digit**3
        n=n//10
        if temp==sum:
            print(i,"is an armstrong number")
            