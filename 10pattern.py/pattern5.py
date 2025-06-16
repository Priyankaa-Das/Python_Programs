#Write a program to draw this pattern without using function:
#   1
#  3 2 3
# 6 5 4 5 6
#10 9 8 7 8 9 10
# Input the number of rows for the pattern
# Input the number of rows for the pattern
rows = 4

# Initialize the starting number
current_number = 1

# Generate the pyramid pattern
for i in range(1, rows + 1):
    # Print leading spaces for pyramid shape
    print(" " * (rows - i), end="")
    
    # Generate the decreasing numbers for the left part of the pyramid
    left_numbers = []
    for j in range(i):
        left_numbers.append(current_number)
        current_number += 1
    
    # Generate the increasing numbers for the right part of the pyramid
    right_numbers = left_numbers[:-1][::-1]
    
    # Combine left and right parts, and print them as a single row
    row_numbers = left_numbers + right_numbers
    print(" ".join(map(str, row_numbers)))
