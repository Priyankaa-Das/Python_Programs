#4 Write a program to print all the ASCII values and their equivalent characters using a while loop. The ASCII values vary from 0 to 255(chr(110) will print ascii character of the value 110. ordi'A') will print corresponding ASCII value of 'A'
for i in range(0,256):
    print(f"ASCII value of {chr(i)} is {i}")