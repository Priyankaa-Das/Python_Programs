class SumSeries:
   
    def calculate_sum(n):
        total = 0
        for i in range(1, n + 1):
            total += i  
        print("Sum:", total)

n = int(input("Enter a number: "))
sumobj = SumSeries
sumobj.calculate_sum(n)

