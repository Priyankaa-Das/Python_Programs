class PriceDiscountCalculator:
    def __init__(self, prices):
        self.prices = prices

    def final_prices(self):
        n = len(self.prices)
        result = self.prices[:]  
        for i in range(n):
            for j in range(i + 1, n):
                if self.prices[j] <= self.prices[i]:
                    result[i] -= self.prices[j]
                    break 
        return result


prices1 = [8, 4, 6, 2, 3]
calc1 = PriceDiscountCalculator(prices1)
print(f"Input: {prices1}")
print("Output:", calc1.final_prices())  


prices2 = [1, 2, 3, 4, 5]
calc2 = PriceDiscountCalculator(prices2)
print(f"\nInput: {prices2}")
print("Output:", calc2.final_prices()) 


prices3 = [10, 1, 1, 6]
calc3 = PriceDiscountCalculator(prices3)
print(f"\nInput: {prices3}")
print("Output:", calc3.final_prices())  