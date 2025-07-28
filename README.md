📚 Library Management System (OOPs in Python)

A simple yet powerful Library Management System built using Python, applying core Object-Oriented Programming (OOP) principles like Encapsulation, Inheritance, Polymorphism, and Abstraction.

This project is part of a learning journey to master OOP in Python and is structured in phases, each representing a key concept.
🚀 Features

    📦 Add books (general and reference)

    ✅ Issue and return books

    📚 View all books with status

    🔁 Polymorphic reading function

    🔐 Encapsulation via getters/setters

    🧬 Inheritance and method overriding

    🧼 Abstract base class for extensibility

🧠 OOP Concepts Used
Concept	Implemented In
Classes & Objects	Book, ReferenceBook, Library
Encapsulation	Private attributes with get_ / set_ methods
Inheritance	ReferenceBook(Book)
Polymorphism	Overridden read() method
Abstraction	Readable (Abstract Base Class)
🗂️ Project Structure

.
├── phase1_classes_objects.py      # Basic class & object structure
├── phase2_encapsulation.py        # Encapsulation using getters/setters
├── phase3_inheritance.py          # Inheritance with base and child classes
├── phase4_polymorphism.py         # Polymorphism with overridden methods
├── phase5_abstraction.py          # Abstraction with ABC class
└── final_project.py               # Complete integrated version

🛠️ How to Run

Make sure you have Python 3.x installed.

python final_project.py

✅ Sample Output

📚 All Books in Library:
📚 Title: Rich Dad Poor Dad, Author: Robert Kiyosaki, Pages: 156, Available: True
📚 Title: Atomic Habits, Author: James Clear, Pages: 320, Available: True
📚 Title: Artificial Intelligence, Author: Kevin Knight, Pages: 1012, Available: True

✅ Book 'Rich Dad Poor Dad' issued successfully!
❌ Cannot issue reference books. They are only available for reading inside the library.
🔄 Book 'Rich Dad Poor Dad' returned successfully!

📖 Starting Reading Session:
📖 Reading book: Rich Dad Poor Dad
📖 Reading book: Atomic Habits
📘 Reading reference book (inside library only): Artificial Intelligence

💡 What You’ll Learn

    How to design and build scalable OOP-based systems

    Importance of each OOP concept in real applications

    Python syntax for OOP best practices

👨‍💻 Author

Shardul Jangam
Aspiring Python Developer · Full Stack Enthusiast
📅 Project Timeline: July 2025
📍 Pune, India
📝 License

This project is open for educational use and demonstration purposes.
