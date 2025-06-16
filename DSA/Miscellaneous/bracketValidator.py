'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    Example 1:
    Input: s = "()"
    Output: true
    Example 2:
    Input: s = "()[]{}"
    Output: true
    Example 3:
    Input: s = "(]"
    Output: false'''

class BracketValidator:
    def __init__(self, s):
        self.s = s
        self.pairs = {')': '(', ']': '[', '}': '{'}

    def is_valid(self):
        stack = []
        for char in self.s:
            if char in self.pairs.values():
                stack.append(char)
            elif char in self.pairs:
                if not stack or stack.pop() != self.pairs[char]:
                    return False
        return not stack

obj = BracketValidator("()")
print(obj.is_valid())  
obj1 = BracketValidator("()[]{}")
print(obj1.is_valid())
obj2 = BracketValidator("(]")
print(obj2.is_valid())        