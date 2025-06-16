import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-']

print("Welcome to Password Generator")
n_letters = int(input("How many letters you want in password?\n"))
n_symbols = int(input("How many symbols you want in password?\n"))
n_numbers = int(input("How many numbers you want in password?\n"))

password = []

for i in range(n_letters):                      # Generate letters
    password.append(random.choice(letters))

for i in range(n_symbols):                      # Generate symbols
    password.append(random.choice(symbols))

for i in range(n_numbers):                      # Generate numbers
    password.append(random.choice(numbers))
    
random.shuffle(password)                        # Shuffle the generated characters
password = ''.join(password)                    # Convert the list to a string
print("Generated Password:", password)