#Write a program to take integer inputs from a file and display sum of the integers.
#Input file: integers.txt : 11 \n 22 \n 33
#Input file format: one integer per line

class intsum:
        
    def readfile():
       with open('integer.txt', 'r') as file:
                content = file.read()
                sum=0
                for i in content.split(','):
                    sum+=int(i)
                print (sum)
                
ob=intsum
ob.readfile()