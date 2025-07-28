'''Your task:
Create 2 classes:

    Book → attributes: title, author, pages, available (default True)

    Library → has a list of books and a method add_book(book)

Then:

    Create 2 book objects

    Add them to the library

    Print the details of all books in the library'''

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.available = True

    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Available: {self.available}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.get_details())

# Creating books
b1 = Book("Rich Dad Poor Dad", "Robert Kiyosaki", 156)
b2 = Book("Atomic Habits", "James Clear", 320)

# Creating Library and adding books
my_library = Library()
my_library.add_book(b1)
my_library.add_book(b2)

# Showing all book details in the library
my_library.show_books()
