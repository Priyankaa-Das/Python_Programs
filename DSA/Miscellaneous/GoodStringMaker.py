'''Given a string s of lower and upper case English letters.
A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
• 0 <= i <= s.length - 2
• s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints. Notice that an empty string is also good.
Example 1:
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
Constraints:
• 1 <= s.length <= 100
• s contains only lower and upper case English letters.'''
class GoodStringMaker:
    def __init__(self, s):
        self.s = s

    def make_good(self):
        stack = []

        for char in self.s:
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()  
            else:
                stack.append(char)

        return ''.join(stack)

s1 = "leEeetcode"
maker1 = GoodStringMaker(s1)
print(f"Input: {s1}")
print("Output:", maker1.make_good())  
