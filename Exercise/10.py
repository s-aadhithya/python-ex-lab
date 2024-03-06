class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print("Title:", book.title)
            print("Author:", book.author)
            print("ISBN:", book.isbn)
            print("Availability:", "Available" if book.availability else "Not Available")
            print()

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.availability:
            self.borrowed_books.append(book)
            book.availability = False
            print("Book", book.title, "borrowed successfully.")
        else:
            print("Book", book.title, "is not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.availability = True
            print("Book", book.title, "returned successfully.")
        else:
            print("Book", book.title, "was not borrowed by this member.")

class LibrarySystem:
    def __init__(self):
        self.library = Library()
        self.members = []

    def register_member(self, member):
        self.members.append(member)

    def display_members(self):
        for member in self.members:
            print("Member ID:", member.member_id)
            print("Name:", member.name)
            print("Borrowed Books:", [book.title for book in member.borrowed_books])
            print()


library_system = LibrarySystem()
book1 = Book("Python Programming", "John Smith", "978-0134444321")
book2 = Book("Data Science for Beginners", "Jane Doe", "978-026253593")
library_system.library.add_book(book1)
library_system.library.add_book(book2)
library_system.library.display_books()
member1 = Member("M001", "Alice")
library_system.register_member(member1)
member1.borrow_book(book1)
library_system.display_members()