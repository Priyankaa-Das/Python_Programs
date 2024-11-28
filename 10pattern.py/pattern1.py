#Write a program for the following pattern:
#A             A
#A  B       B  A
#A  B   C   B  A

n = int(input("Enter the range: "))  # Input the number of rows
for i in range(n):
    for j in range(2 * n - 1):  # Loop through columns
        if j == i or j == 2 * n - 2 - i:  # Left and right diagonals
            print(chr(65 + i), end=' ')  # Print letters based on row index
        elif i < n and (j > i and j < 2 * n - 2 - i):  # Middle part
            print(chr(65 + (j - i)), end=' ')
        else:
            print(' ', end=' ')  # Fill with spaces
    print()  # Move to the next line

