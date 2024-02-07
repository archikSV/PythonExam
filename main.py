print("Part 1: Python Basic")
print("Task 4")

"""
Напишіть програму, яка створює список цілих чисел та
виводить новий список, який містить лише парні числа з
вихідного списку.
"""

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Printing a new list containing only the even numbers from the original list
even_numbers_list = [num for num in original_list if num % 2 == 0]
print(even_numbers_list)