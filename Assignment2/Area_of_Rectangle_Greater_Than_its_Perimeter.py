#Given the length and breadth of a rectangle, write a program whether the area of a rectangle is greater than its perimeter.For example the area of a triangle with length=5 and breadth=4 is greater than its perimeter.
#Area of rectangle = length * breadth
#Perimeter of rectangle = 2 * (length + breadth)
length = int(input("Enter the length of the rectangle: "))
breadth=int(input("Enter the breadth of the rectangle: "))
area = length * breadth
perimeter = 2 * (length + breadth)
if area > perimeter:
    print("The area of the rectangle is greater than its perimeter.")
else:
    print("The perimeter of the rectangle is greater than or equal to its area.")