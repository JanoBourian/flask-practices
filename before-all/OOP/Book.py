class Book:
    TYPES = ("hardcover", "paperback")
    
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
        
    def __str__(self):
        return f"<Book {self.name}, {self.book_type}, {self.weight}>"
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)

print(Book.TYPES)
book = Book("Harry potter", "hardcover", 1500)
print(book.name)
print(book)
book_2 = Book.hardcover("Twlight", 1700)
print(book_2)
book_3 = Book.paperback("Dune", 1000)
print(book_3)