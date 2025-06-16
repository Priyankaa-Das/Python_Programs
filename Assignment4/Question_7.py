def is_palindrome(number):
    str_number = str(number)
    reversed_number = ""
    for char in str_number:
        reversed_number = char + reversed_number
    return str_number == reversed_number

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
