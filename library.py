#!/usr/bin/python3
class Book:
    def __init__(self, title, author, isbn, available_copies):
        """Initialize a Book object with title, author, ISBN, and available copies.
        Args:
        - title (str): Title of the book.
        - author (str): Author of the book.
        - isbn (str): ISBN of the book.
        - available_copies (int): Number of available copies.

        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies

    def borrow_a_book(self):
        """Borrow a book if there are available copies.

        Returns:
        - bool: True if the book is successfully borrowed, False otherwise.

        """
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        else:
            print("No available copies to borrow.")
            return False

    def return_a_book(self):
        """Return a book, incrementing the available copies.

        Returns:
        - bool: True if the book is successfully returned.

        """
        self.available_copies += 1
        return True

class User:
    def __init__(self, name):
        """Initialize a User object with a name and an empty list of borrowed books.

        Args:
        - name (str): Name of the user.

        """
        self.name = name
        self.books_borrowed = []

    def borrow_a_book(self, book):
        """Borrow a book and add it to the user's list of borrowed books.

        Args:
        - book (Book): Book object to be borrowed.

        Returns:
        - bool: True if the book is successfully borrowed, False otherwise.

        """
        if isinstance(book, Book) and book.borrow_a_book():
            self.books_borrowed.append(book)
            return True
        else:
            print("Unable to borrow the book.")
            return False

    def return_a_book(self, book):
        """Return a book and remove it from the user's list of borrowed books.

        Args:
        - book (Book): Book object to be returned.

        Returns:
        - bool: True if the book is successfully returned, False otherwise.

        """
        if book in self.books_borrowed and book.return_a_book():
            self.books_borrowed.remove(book)
            return True
        else:
            print("Unable to return the book.")
            return False

class Library:
    def __init__(self):
        """Initialize a Library object with an empty list of books.

        """
        self.books = []

    def add_book(self, book):
        """Add a book to the library's collection.

        Args:
        - book (Book): Book object to be added.

        Returns:
        - bool: True if the book is successfully added, False otherwise.

        """
        if isinstance(book, Book):
            self.books.append(book)
            return True
        else:
            print("This is not a book!")
            return False

    def remove_book(self, book):
        """Remove a book from the library's collection.

        Args:
        - book (Book): Book object to be removed.

        Returns:
        - bool: True if the book is successfully removed, False otherwise.

        """
        if isinstance(book, Book):
            self.books.remove(book)
            return True
        else:
            print("This is not a book!")
            return False

    def display_available_books(self):
        """Display the titles and authors of available books in the library.

        """
        print("Available Books:")
        for book in self.books:
            print(f"{book.title} by {book.author}")

