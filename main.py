print("Part 1: Python Basic")
print("Task 7")

"""
(додаткове на кристалики)
Напишіть програму, яка
створює словник, де ключами є слова, а значеннями - їхні
визначення. Дозвольте користувачу додавати, видаляти
та шукати слова у цьому словнику.
"""

dictionary = {}

def add_word_definition(word, definition):
    dictionary[word] = definition

def delete_word(word):
    if word in dictionary:
        del dictionary[word]
    else:
        print(f"The word '{word}' does not exist in the dictionary.")

def search_word(word):
    if word in dictionary:
        print(f"The definition of '{word}' is: {dictionary[word]}")
    else:
        print(f"The word '{word}' does not exist in the dictionary.")

while True:
    print("\n1. Add a word and its definition")
    print("2. Delete a word")
    print("3. Search for a word")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        word = input("Enter the word: ")
        definition = input("Enter the definition: ")
        add_word_definition(word, definition)
    elif choice == 2:
        word = input("Enter the word to delete: ")
        delete_word(word)
    elif choice == 3:
        word = input("Enter the word to search: ")
        search_word(word)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")