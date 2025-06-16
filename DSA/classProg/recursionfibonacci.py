# 3.Use recursion to print fibonacci series.
# 0,1,1,2,3,5,8,13
class recursion_fibonacci:
    def __init__(self,n):
        self.n=n
    
    def fibonacci(self,n):
        if n <= 0:
            return "Input should be a positive integer."
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)
        
        def display(self):
            for i in range(1,self.n+1):
                print(self.fibonacci(i),end=" ")
            
        
ob=recursion_fibonacci(5)
ob.display()