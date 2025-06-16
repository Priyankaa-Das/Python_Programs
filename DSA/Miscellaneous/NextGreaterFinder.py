'''Q3. The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. 
If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
            • 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
            • 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
            • 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
            • 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
            • 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.'''
class NextGreaterFinder:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2

    def find_next_greater(self):
        stack = []
        next_greater_map = {}

        for num in self.nums2:
            while stack and stack[-1] < num:
                prev = stack.pop()
                next_greater_map[prev] = num
            stack.append(num)

        for num in stack:
            next_greater_map[num] = -1

        result = [next_greater_map[num] for num in self.nums1]
        return result

    def display(self):
        print("Nums1:", self.nums1)
        print("Nums2:", self.nums2)
        print("Next greater elements:", self.find_next_greater())

obj1 = NextGreaterFinder(nums1=[4,1,2], nums2=[1,3,4,2])
obj1.display()

obj2 = NextGreaterFinder(nums1=[2,4], nums2=[1,2,3,4])
obj2.display()