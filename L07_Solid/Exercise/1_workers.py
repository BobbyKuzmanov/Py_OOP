class Book:

    def __init__(self, content):
        self.content = content


class Formatter:

    def format(self, book):
        return book.content


class Printer:

    def get_book(self, book, formatter):
        return formatter.format(book)


book = Book("book")
formatter = Formatter()
printer = Printer()

print(printer.get_book(book, formatter))

# You are provided with a code on which you have to apply the DIP (Dependency Inversion Principle) so that
# when adding new worker classes, the Manager class will work properly.

# Output:
# I'm working!!
# manager fails to support super_worker....