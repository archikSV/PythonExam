print("Part 1: Python Basic")
print("Task 5")

"""
Напишіть функцію, яка приймає список рядків від
користувача і повертає новий список, що містить лише
рядки, що починаються з великої літери.
"""

def filter_capitalized_strings(input_list):
    return [s for s in input_list if s[0].isupper()]

input_list = ["Jeremy", "Hobkins", "is", "the", "Best"]
result = filter_capitalized_strings(input_list)
print(result)  # Output: ['Jeremy', 'Hobkins', 'Best']