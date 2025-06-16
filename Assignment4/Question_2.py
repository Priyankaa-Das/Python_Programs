#Write a program to check if given  number is even or odd using the function.
def evenodd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"

num=int(input("Enter number to check even odd: "))
print("The number is ",evenodd(num))