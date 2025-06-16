# 1. Write a program to implement infix to postfix transformation.

class InfixToPostfix:
    def __init__(self, infix):
        self.infix = infix
        self.postfix = []
        self.stack = []  
        
    def precedence(self, char):
        if char in ('+', '-'):
            return 1
        elif char in ('*', '/','%'):
            return 2
        elif char in ('^'): 
            return 3
        return 0

    def infix_to_postfix(self):
        for i in self.infix:
            if i.isalpha():  
                self.postfix.append(i)
            elif i == '(':  
                self.stack.append(i)
            elif i == ')':  
                while self.stack and self.stack[-1] != '(':
                    self.postfix.append(self.stack.pop())
                self.stack.pop() 
            else:  
                while self.stack and self.precedence(i) <= self.precedence(self.stack[-1]):
                    self.postfix.append(self.stack.pop())
                self.stack.append(i)

        while self.stack:
            self.postfix.append(self.stack.pop())

    def display(self):
        print("Infix Expression: ", "".join(self.infix))
        print("Postfix Expression: ", "".join(self.postfix))



l = ['A', '+', 'B', '*', '(', 'C', '-', 'D', ')','-', 'E', '/', 'F']
obj = InfixToPostfix(l)
obj.infix_to_postfix()
obj.display()