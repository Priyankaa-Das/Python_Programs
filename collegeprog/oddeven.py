#4) given number=4247638. Now add +1 to the oddigits and add +2 to the even digits.print the updated numbers.Remember that 9+1 or 9+2 will result in 0.
# 4+2=6, 2+2=4, 4+2=6, 7+1=8, 6+2=8, 3+1=4, 8+2=0
# Output: 6468840
n=4247638
updatednumber=""
for i in str(n):
    i=int(i)
    if i%2==0:
        even=i+2
        if even >= 10:
            even=0
        updatednumber=updatednumber + str(even)
    else:
        odd=i+1
        if odd >= 10:
            odd=0
        updatednumber=updatednumber + str(odd)
print(updatednumber)