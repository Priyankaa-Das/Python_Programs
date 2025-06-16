#Given three points(x1,y1),(x2,y2)and(x3,y3),write a program to check if all the three points fall on one straight line.
x1=input("Enter the x1 point: ")
y1=input("Enter the y1 point: ")
x2=input("Enter the x2 point: ")
y2=input("Enter the y2 point: ")
x3=input("Enter the x3 point: ")
y3=input("Enter the y3 point: ")
if (y2 - y1)/(x2 - x1) == (y3 - y2)/(x3 - x2):
    print("All three points fall on one straight line")
else:
    print("All three points do not fall on one straight line")
    