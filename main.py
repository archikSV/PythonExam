print("Part 1: Python Basic")
print("Task 1")

"""
Напишіть програму, яка приймає два цілих числа від
користувача і виводить суму діапазону чисел між ними.
"""


# Ask the user for two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Find the minimum and maximum values
min_num = min(num1, num2)
max_num = max(num1, num2)

# Find the sum of the range of numbers between them
total_sum = sum(range(min_num + 1, max_num))

# Print the sum
print(f"The sum of the range of numbers between {min_num} and {max_num} is {total_sum}")