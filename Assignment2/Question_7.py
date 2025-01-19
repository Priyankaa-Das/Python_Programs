#7.Write a program to check whether a triangle is valid or not,when the three angles of the triangle is entered through a keyboard.A triangle is valid if the sum of three angles is equal to 180 degrees.
a1=int(input("Enter the first angle:"))
a2=int(input("Enter the second angle:"))
a3=int(input("Enter the third angle:"))
sum=a1+a2+a3
if sum==180:
    print("The triangle is valid")
else:
    print("The triangle is not valid")