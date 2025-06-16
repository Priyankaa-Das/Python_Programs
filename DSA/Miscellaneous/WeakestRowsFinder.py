class WeakestRowsFinder:
    def __init__(self, mat):
        self.mat = mat

    def count_soldiers(self, row):
        left, right = 0, len(row)
        while left < right:
            mid = (left + right) // 2
            if row[mid] == 1:
                left = mid + 1
            else:
                right = mid
        return left

    def k_weakest_rows(self, k):
        strength = []
        for i, row in enumerate(self.mat):
            soldiers = self.count_soldiers(row)
            strength.append((soldiers, i)) 
        strength.sort()
        return [idx for _, idx in strength[:k]]

mat = [
    [1,1,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,1,1,1,1]
]
k = 3

finder = WeakestRowsFinder(mat)
print(finder.k_weakest_rows(k)) 