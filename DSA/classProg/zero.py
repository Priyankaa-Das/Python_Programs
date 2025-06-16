#Find the number of zeros in a list.
class zero:
    def __init__(self,list):
        self.list=list
    def count_zeros(self):
        return self.list.count(0)
       
ob=zero([1,2,0,0,4,0])
print(ob.count_zeros())  