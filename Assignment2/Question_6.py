#6.If the ages of Ram,Shyam and Ajay are input through the keyboard,write a program to find the youngest of three.
r=input("Enter Ram's age:")
s=input("Enter Shyam's age:")
a=input("Enter Ajay's age:")
print("Ram is the youngest" if r < s and r < a else "Shyam is the youngest" if s < r and s < a else "Ajay is the youngest")