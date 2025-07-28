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

# ✅ Inheriting from Book and overriding set_available
class ReferenceBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author, pages)

    def set_available(self, status):
        if not status:
            print("❌ Cannot issue reference books. They are only available for reading inside the library.")
        else:
            print("✅ Reference books are always available in the library.")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):  # Handles both Book and ReferenceBook
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.get_details())

# Creating normal books
b1 = Book("Rich Dad Poor Dad", "Robert Kiyosaki", 156)
b2 = Book("Atomic Habits", "James Clear", 320)

# Creating reference book
rb1 = ReferenceBook("Artificial Intelligence", "Kevin Knight", 1012)

# Creating Library and adding books
my_library = Library()
my_library.add_book(b1)
my_library.add_book(b2)
my_library.add_book(rb1)

# Try issuing books
b1.set_available(False)
rb1.set_available(False)  # This will print the message and deny issuing

# Check book's title and availability
print(b1.get_title())       # Rich Dad Poor Dad
print(b1.get_available())   # False
print(rb1.get_title())      # Artificial Intelligence
print(rb1.get_available())  # True (still available)

# Show all books
my_library.show_books()
