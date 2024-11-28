#Given three points (x1,y1),(x2,y2) and (x3,y3),write a program to check if all three points fall on one straight line.
#The points are said to be collinear if the slope of the line joining any two points is equal to the slope of the line joining the third point with either of the first two points.
#Area=21​×|x1(y2−y3)+x2(y3−y1)+x3(y1−y2)|
x1, y1 = map(int, input("Enter coordinates of the first point (x1 y1): ").split())
x2, y2 = map(int, input("Enter coordinates of the first point (x1 y1): ").split())
x3, y3 = map(int, input("Enter coordinates of the first point (x1 y1): ").split())
area = x1 * ((y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
