'''Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:
• 1 <= nums1.length, nums2.length <= 1000
• 0 <= nums1[i], nums2[i] <= 1000'''
class ArrayIntersection:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2

    def get_intersection(self):
        set1 = set(self.nums1)
        set2 = set(self.nums2)
        return list(set1 & set2)

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
intersect1 = ArrayIntersection(nums1, nums2)
print("Output:", intersect1.get_intersection()) 