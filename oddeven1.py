n = int(input("Enter number: "))
updatednumber = 0
place = 1  

while n > 0:
    i = n % 10  
    n //= 10        

    if i % 2 == 0:  
        num = i + 2
        if num >= 10:
            even = 0
    else:  
        num = i + 1
        if num >= 10:
            num = 0

    updatednumber += num * place
    place *= 10  

print("Updated number:", updatednumber)
