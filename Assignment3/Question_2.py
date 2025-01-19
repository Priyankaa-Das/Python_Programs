#Write a program to find the factorial value of any number entered through the keyboard
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
    print("Factorial of", num, "is", fact)
    