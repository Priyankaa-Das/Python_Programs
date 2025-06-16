""" Sorts an array using the insertion sort algorithm."""

class InsertionSort:
    def __init__(self, lst):
        self.lst = lst

    def insertion_sort(self):
        l = len(self.lst)
        i = 1
        while i < l:
            item = self.lst[i]
            index = i - 1
            while index >= 0 and self.lst[index] > item:
                self.lst[index + 1] = self.lst[index]
                index = index - 1
            self.lst[index + 1] = item
            i = i + 1
        return self.lst


obj = InsertionSort([5, 2, 9, 1, 5, 6])
print("Before sorting:", obj.lst)
print("After sorting:", obj.insertion_sort())