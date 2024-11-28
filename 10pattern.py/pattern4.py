#Write a program to draw this pattern without using function:
#      1
#    3 2
#  6 5 4
#10 9 8 7

rows = 4
current_number = 1
for i in range(1, rows + 1):
    print(" " * (rows - i) * 2, end="")
    row_numbers = []
    for j in range(i):
        row_numbers.append(current_number)
        current_number += 1
    row_numbers.reverse() 
    print(" ".join(map(str, row_numbers)))