# 2. Write a program to evaluate a postfix expression.
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

    def evaluate_postfix(self):
        stack = []
        operators = {'+': lambda x, y: x + y,
                     '-': lambda x, y: x - y,
                     '*': lambda x, y: x * y,
                     '/': lambda x, y: x / y,
                     '%': lambda x, y: x % y,
                     '^': lambda x, y: x ** y}  

        for char in self.postfix:
            if char.isalpha():
                try:
                    val = int(input(f"Enter the value of {char}: "))
                    stack.append(val)
                except ValueError:
                    print("Invalid input. Please enter an integer.")
                    return None  
            elif char in operators:
                try:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = operators[char](operand1, operand2)
                    stack.append(result)
                except IndexError:
                    print("Invalid postfix expression.")
                    return None
            
        return stack.pop() if stack else None


l = ['A', '+', 'B', '*', '(', 'C', '-', 'D', ')','-', 'E', '/', 'F']
obj = InfixToPostfix(l)
obj.infix_to_postfix()
obj.display()
result = obj.evaluate_postfix()
if result is not None:
    print("Result of postfix evaluation:", result)