#1.Write a program to calculate overtime pay of 10 employees. 
# Overtime is paid at the rate of Rs. 12.00 per hour for every hour worked above 40 hours.
# Assume that employees do not work for fractional part of an hour.
for i in range (11):
    hrs=int(input("Enter the hrs: "))
    pay=0
    if hrs>40:
        pay=(hrs-40)*12
        print("Overtime pay is: ",pay)
    else:
        print("Overtime pay: ",pay)