#Write a program to read a text file from the local drive and display the content of the file.

class readtext:
    def __init__(self, filename):
        self.filename = filename
        
    def readfile(self):
            with open(self.filename, 'r') as file:
                content = file.read()
                return content

ob=readtext('sample.txt')
print(ob.readfile())