class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print(f"Title:{self.title},Author:{self.author},ISBN:{self.isbn}")

class Library:
    def __init__(self):
        self.books =[]

    def add_book(self,book):
        self.book.append(book)
        print(f"Book{book.title} added to the Library")

    def remove_book(self,isbn):
        book_to_remove = None
        for book in self.books:
            if book.isbn ==isbn:
                book_to_remove = book
        
        if book_to_remove:
            self.books.remove(book_to_remove)
            print(f"Book{book_to_remove.title} removed from the Library")

    def display_books(self):
        if not self.boooks:
            print("No Books in the library")
        else:
            for book in self.books:
                book.display_info()

book1 = Book(title="Azure OpenAI",author="Hari",isbn="123")
book2 = Book(title= "AWS Lambda",author="Ram",isbn="456")

my_library =Library()

my_library.add_book(book1)
my_library.add_book(book2)

my_library.display_books()

my_library.remove_book("123")

my_library.display_books()