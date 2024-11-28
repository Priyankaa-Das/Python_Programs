#Print a series of all nummbers between 100 and 700 which are divisible by 12.
#n=int(input("Enter the range: "))
for i in range(100,701):
    if i%12==0:
        print(i, end=" ")