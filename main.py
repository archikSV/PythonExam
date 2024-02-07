print("Part 2: Python OOP")
print("Task 1")

"""
Симулятор роботи сайту
WebSite: Основний клас, який представляє вебсайт.
Атрибути: назва сайту, URL, список сторінок.
Методи: додавання/видалення сторінок, відображення
інформації про сайт.
WebPage: Клас, який представляє окрему сторінку на сайті.
Атрибути: заголовок сторінки, вміст, дата публікації.
Методи: відображення деталей сторінки.

Реалізація функціональності:
Дозвольте користувачеві створювати новий сайт з
певною назвою та URL. Додайте можливість створювати нові
сторінки для сайту, вводячи заголовок та вміст. Реалізуйте
функцію для видалення сторінок з сайту. Включіть функцію
для відображення всієї інформації про сайт, включаючи
список усіх сторінок.

Розробіть простий текстовий інтерфейс для взаємодії з
користувачем. Користувач повинен мати змогу вибирати дії,
такі як створення сайту, додавання/видалення сторінок,
перегляд інформації про сайт.

Додаткові можливості (за бажанням на кристалики):
Реалізуйте систему логіну/реєстрації для керування
сайтом. Додайте можливість редагування існуючих сторінок.
Створіть функціонал для пошуку сторінок за ключовими
словами у заголовку або вмісті.
"""

import datetime

class WebPage: # Клас, який представляє окрему сторінку на сайті.
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.publication_date = datetime.datetime.now()

    def display_page_details(self): # Відображення деталей сторінки.
        print(f"Заголовок: {self.title}")
        print(f"Вміст: {self.content}")
        print(f"Дата публікації: {self.publication_date.strftime('%Y-%m-%d %H:%M:%S')}")

class WebSite: # Основний клас, який представляє вебсайт.
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.pages = []

    def add_page(self, title, content): # Додавання сторінки.
        new_page = WebPage(title, content)
        self.pages.append(new_page)
        print("Сторінка успішно додана.")

    def remove_page(self, title): # Видалення сторінки.
        for page in self.pages:
            if page.title == title:
                self.pages.remove(page)
                print("Сторінка успішно видалена.")
                return
        print("Сторінка не знайдена.")

    def edit_page(self, title, new_title, new_content): # Редагування сторінки.
        for page in self.pages:
            if page.title == title:
                page.title = new_title
                page.content = new_content
                print("Сторінка успішно відредагована.")
                return
        print("Сторінка не знайдена.")

    def search_pages(self, keyword): # Пошук сторінок за ключовими словами.
        found_pages = []
        for page in self.pages:
            if keyword in page.title or keyword in page.content:
                found_pages.append(page)
        if found_pages:
            print(f"Знайдені сторінки за ключовим словом '{keyword}':")
            for page in found_pages:
                page.display_page_details()
        else:
            print(f"Сторінки за ключовим словом '{keyword}' не знайдено.")

    def display_site_info(self): # Відображення інформації про сайт.
        print(f"Назва сайту: {self.name}")
        print(f"URL: {self.url}")
        print("Сторінки:")
        for page in self.pages:
            page.display_page_details()

class User: # Клас, який представляє користувача сайту.
    def __init__(self, username, password):
        self.username = username
        self.password = password

class WebsiteManagementSystem: # Система керування вебсайтом.
    def __init__(self):
        self.users = []

    def register_user(self, username, password): # Реєстрація нового користувача.
        new_user = User(username, password)
        self.users.append(new_user)
        print("Користувач успішно зареєстрований.")

    def login(self, username, password): # Вхід користувача.
        for user in self.users:
            if user.username == username and user.password == password:
                print("Вхід успішний.")
                return True
        print("Неправильне ім'я користувача або пароль.")
        return False

def main():
    website_management_system = WebsiteManagementSystem()
    website = None
    logged_in = False
    while True:
        print("\n1. Зареєструвати користувача")
        print("2. Увійти")
        print("3. Створити новий сайт")
        print("4. Додати сторінку")
        print("5. Редагувати сторінку")
        print("6. Видалити сторінку")
        print("7. Пошук сторінок за ключовими словами")
        print("8. Переглянути інформацію про сайт")
        print("9. Вийти")
        choice = input("Виберіть дію: ")

        if choice == '1':
            username = input("Введіть ім'я користувача: ")
            password = input("Введіть пароль: ")
            website_management_system.register_user(username, password)
        elif choice == '2':
            if not logged_in:
                username = input("Введіть ім'я користувача: ")
                password = input("Введіть пароль: ")
                logged_in = website_management_system.login(username, password)
            else:
                print("Ви вже увійшли.")
        elif choice == '3':
            if logged_in:
                name = input("Введіть назву сайту: ")
                url = input("Введіть URL сайту: ")
                website = WebSite(name, url)
                print("Сайт успішно створено.")
            else:
                print("Спочатку увійдіть.")
        elif choice == '4':
            if logged_in:
                if website:
                    title = input("Введіть заголовок сторінки: ")
                    content = input("Введіть вміст сторінки: ")
                    website.add_page(title, content)
                else:
                    print("Спочатку створіть сайт.")
            else:
                print("Спочатку увійдіть.")
        elif choice == '5':
            if logged_in:
                if website:
                    title = input("Введіть заголовок сторінки для редагування: ")
                    new_title = input("Введіть новий заголовок сторінки: ")
                    new_content = input("Введіть новий вміст сторінки: ")
                    website.edit_page(title, new_title, new_content)
                else:
                    print("Спочатку створіть сайт.")
            else:
                print("Спочатку увійдіть.")
        elif choice == '6':
            if logged_in:
                if website:
                    title = input("Введіть заголовок сторінки для видалення: ")
                    website.remove_page(title)
                else:
                    print("Спочатку створіть сайт.")
            else:
                print("Спочатку увійдіть.")
        elif choice == '7':
            if logged_in:
                if website:
                    keyword = input("Введіть ключове слово для пошуку: ")
                    website.search_pages(keyword)
                else:
                    print("Спочатку створіть сайт.")
            else:
                print("Спочатку увійдіть.")
        elif choice == '8':
            if logged_in:
                if website:
                    website.display_site_info()
                else:
                    print("Спочатку створіть сайт.")
            else:
                print("Спочатку увійдіть.")
        elif choice == '9':
            break
        else:
            print("Невідома команда.")

if __name__ == "__main__":
    main()