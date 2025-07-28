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

# Issue a book (change availability)
b1.set_available(False)

# Check book's title and availability
print(b1.get_title())      # ➜ Rich Dad Poor Dad
print(b1.get_available())  # ➜ False

# Show all books in the library
my_library.show_books()
