'''Write a function that takes a string as a parameter and returns a string
with every successive repetitive character replaced with a star(*). For
example, ‘balloon’ is returned as ‘bal*o*n’.'''

class Balloon:
    def __init__(self):
        pass
    
    def replace_repetitive_chars(s):
        result = s[0]  
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:  
                result += '*'
            else:
                result += s[i]
        print("Modified String:", result )


text = input("Enter a string: ")
obj= Balloon
obj.replace_repetitive_chars(text)

