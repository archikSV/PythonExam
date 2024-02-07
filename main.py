print("Part 1: Python Basic")
print("Task 6")

"""
Напишіть функцію, яка приймає список рядків від
користувача і повертає новий список, що містить лише
рядки, які містять слово "Python".
"""

def filter_python_strings(input_list):
    return [string for string in input_list if "Python" in string]

input_list = ["I love Python", "Python is great", "Java is not Python", "Java is not Great"]
filtered_list = filter_python_strings(input_list)
print(filtered_list) # Output: ['I love Python', 'Python is great', 'Java is not Python']
