from abc import ABC, abstractmethod

# Abstract Base Class
class Readable(ABC):
    @abstractmethod
    def read(self):
        pass

# Book class (Encapsulation + Abstraction)
class Book(Readable):
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
        return f"📚 Title: {self.__title}, Author: {self.__author}, Pages: {self.__pages}, Available: {self.__available}"

    def read(self):
        return f"📖 Reading book: {self.__title}"

# ReferenceBook class (Inheritance + Polymorphism)
class ReferenceBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author, pages)

    def set_available(self, status):
        if not status:
            print("❌ Cannot issue reference books. They are only available for reading inside the library.")
        else:
            print("✅ Reference books are always available in the library.")

    def read(self):
        return f"📘 Reading reference book (inside library only): {self.get_title()}"

# Library class (Manages collection of books)
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print("\n📚 All Books in Library:")
        for book in self.books:
            print(book.get_details())

    def issue_book(self, title):
        for book in self.books:
            if book.get_title().lower() == title.lower():
                if isinstance(book, ReferenceBook):
                    book.set_available(False)
                    return
                if book.get_available():
                    book.set_available(False)
                    print(f"✅ Book '{title}' issued successfully!")
                else:
                    print(f"❌ Book '{title}' is currently not available.")
                return
        print(f"❌ Book '{title}' not found in library.")

    def return_book(self, title):
        for book in self.books:
            if book.get_title().lower() == title.lower():
                book.set_available(True)
                print(f"🔄 Book '{title}' returned successfully!")
                return
        print(f"❌ Book '{title}' not found in library.")

# Polymorphic function
def start_reading(book):
    print(book.read())

# ------------------------------
# ✅ Sample Usage / Test Cases
# ------------------------------

if __name__ == "__main__":
    # Create Library
    my_library = Library()

    # Create Books
    b1 = Book("Rich Dad Poor Dad", "Robert Kiyosaki", 156)
    b2 = Book("Atomic Habits", "James Clear", 320)
    rb1 = ReferenceBook("Artificial Intelligence", "Kevin Knight", 1012)

    # Add to library
    my_library.add_book(b1)
    my_library.add_book(b2)
    my_library.add_book(rb1)

    # Display all books
    my_library.show_books()

    # Issue book
    my_library.issue_book("Rich Dad Poor Dad")
    my_library.issue_book("Artificial Intelligence")  # Should show restriction

    # Return book
    my_library.return_book("Rich Dad Poor Dad")

    # Polymorphic Reading
    print("\n📖 Starting Reading Session:")
    for book in my_library.books:
        start_reading(book)
