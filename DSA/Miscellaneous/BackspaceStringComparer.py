class BackspaceStringComparer:
    def __init__(self, s, t):
        self.s = s
        self.t = t

    def _process(self, text):
        stack = []
        for char in text:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

    def compare(self):
        processed_s = self._process(self.s)
        processed_t = self._process(self.t)
        return processed_s == processed_t


s1 = "ab#c"
t1 = "ad#c"
comparer1 = BackspaceStringComparer(s1, t1)
print(f"Input: s = {s1}, t = {t1}")
print("Output:", comparer1.compare())  

s2 = "ab##"
t2 = "c#d#"
comparer2 = BackspaceStringComparer(s2, t2)
print(f"\nInput: s = {s2}, t = {t2}")
print("Output:", comparer2.compare())  

s3 = "a#c"
t3 = "b"
comparer3 = BackspaceStringComparer(s3, t3)
print(f"\nInput: s = {s3}, t = {t3}")
print("Output:", comparer3.compare())  
