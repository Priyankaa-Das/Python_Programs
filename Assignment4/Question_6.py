def calculate_sums(numbers):
    sum_positive = sum(num for num in numbers if num > 0)
    sum_negative = sum(num for num in numbers if num < 0)
    return sum_positive, sum_negative

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
positive_sum, negative_sum = calculate_sums(numbers)

print("Sum of positive numbers: ",positive_sum)
print("Sum of negative numbers: ",negative_sum)
