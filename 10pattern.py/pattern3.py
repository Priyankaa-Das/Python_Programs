#WAP to draw the pattern:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
rows = int(input("Enter the range: "))
for i in range(rows):
    for j in range(i + 1): 
        num = 1
        if j > i - j:  
            j = i - j
        for k in range(j):
            num = num * (i - k)
            num = num // (k + 1)
        print(num, end=" ")
    print()
