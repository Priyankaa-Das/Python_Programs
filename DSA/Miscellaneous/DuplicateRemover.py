class DuplicateRemover:
    def __init__(self, s):
        self.s = s

    def remove_duplicates(self):
        stack = []
        for char in self.s:
            if stack and stack[-1] == char:
                stack.pop()  
            else:
                stack.append(char)
        return ''.join(stack)


s1 = "abbaca"
remover1 = DuplicateRemover(s1)
print(f"Input: {s1}")
print("Output:", remover1.remove_duplicates()) 


s2 = "azxxzy"
remover2 = DuplicateRemover(s2)
print(f"\nInput: {s2}")
print("Output:", remover2.remove_duplicates())  