print("Part 1: Python Basic")
print("Task 2")

"""
Напишіть програму, для знаходження суми всіх парних
чисел від 1 до 100.
"""

# Initialize sum
total_sum = 0

# Iterate through numbers from 1 to 100
for i in range(1, 101):
    # Check if the number is even
    if i % 2 == 0:
        # Add the even number to the total sum
        total_sum += i

# Print the total sum of even numbers
print(total_sum)