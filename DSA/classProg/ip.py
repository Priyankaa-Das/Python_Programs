class InfixToPostfix:
    def __init__(self, infix):
        self.infix = infix
        self.postfix = []
        self.stack = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def infix_to_postfix(self):
        for char in self.infix:
            if char.isalpha():
                self.postfix.append(char)
            elif char == '(':
                self.stack.append(char)
            elif char == ')':
                while self.stack and self.stack[-1] != '(':
                    self.postfix.append(self.stack.pop())
                if self.stack and self.stack[-1] == '(':
                    self.stack.pop()
            else:
                while self.stack and self.stack[-1] in self.precedence and self.precedence[self.stack[-1]] >= self.precedence[char]:
                    self.postfix.append(self.stack.pop())
                self.stack.append(char)
                
        while self.stack:
            self.postfix.append(self.stack.pop())
            
        def display(self):
            print("Infix:", self.infix)
            print("Postfix:", self.postfix)

l = ['A', '+', 'B', '*', '(', 'C', '-', 'D', ')','-', 'E', '/', 'F']
obj = InfixToPostfix(l)
obj.infix_to_postfix()
obj.display()