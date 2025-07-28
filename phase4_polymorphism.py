# phase4_polymorphism.py

class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages
        self.__available = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_pages(self):
        return self.__pages

    def get_available(self):
        return self.__available

    def set_available(self, status):
        self.__available = status

    def get_details(self):
        return f"Title: {self.__title}, Author: {self.__author}, Pages: {self.__pages}, Available: {self.__available}"

    def read(self):
        return f"Reading book: {self.__title}"

class ReferenceBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author, pages)

    def set_available(self, status):
        if not status:
            print("❌ Cannot issue reference books. They are only available for reading inside the library.")
        else:
            print("✅ Reference books are always available in the library.")

    def read(self):
        return f"Reading reference book (inside library only): {self.get_title()}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.get_details())

# Polymorphic function
def start_reading(book):
    print(book.read())

# Creating books
b1 = Book("Rich Dad Poor Dad", "Robert Kiyosaki", 156)
b2 = Book("Atomic Habits", "James Clear", 320)
rb1 = ReferenceBook("Artificial Intelligence", "Kevin Knight", 1012)

# Creating Library and adding books
my_library = Library()
my_library.add_book(b1)
my_library.add_book(b2)
my_library.add_book(rb1)

# Demonstrating polymorphism
start_reading(b1)   # Reading book: Rich Dad Poor Dad
start_reading(rb1)  # Reading reference book (inside library only): Artificial Intelligence
