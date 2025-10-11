# library_system.py

# Base Class
class Book:
    def __init__(self, title, author):
        """
        Initialize the Book with common attributes.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Return a readable string representation of a Book.
        """
        return f"Book: {self.title} by {self.author}"


# Derived Class: EBook inherits from Book
class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook, reusing Book's attributes (title, author)
        and adding a unique one (file_size).
        """
        # Call the parent constructor (Book)
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Return details of the EBook.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived Class: PrintBook inherits from Book
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook with Book attributes plus page_count.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Return details of the PrintBook.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition Class: Library
class Library:
    def __init__(self):
        """
        The Library holds a collection (list) of Book, EBook, or PrintBook instances.
        """
        self.books = []  # composition: Library "has" books

    def add_book(self, book):
        """
        Add a Book, EBook, or PrintBook to the library.
        """
        self.books.append(book)

    def list_books(self):
        """
        List all books currently in the library.
        """
        for book in self.books:
            print(book)
