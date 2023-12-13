class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.page = pages


class Library:

    def __init__(self, location):
        self.location = location
        self.books = []

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book

        return "No such book"

    def add_book(self, book):
        self.books.append(book)


class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

class Reader(Person):
    def __init__(self, name, age, address, current_book):
        super().__init__(name, age, address)
        self.current_book = current_book
        self.current_page = None

    def turn_page(self):
        if self.current_page:
            self.current_page += 1
            return
        self.current_page = 1



library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "A1")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "B2")
book3 = Book("1984", "George Orwell", "C3")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

title_to_find = "To Kill a Mockingbird"
found_book = library.find_book(title_to_find)

if found_book:
    print(f"Book found: {found_book}")
else:
    print(f"Book with title '{title_to_find}' not found.")
