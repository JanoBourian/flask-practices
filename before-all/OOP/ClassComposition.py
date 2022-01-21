from typing import List

# class BookShelf:
#     def __init__(self, quantity):
#         self.quantity = quantity

#     def __str__(self):
#         return f"<BookShelf with {self.quantity} books>"

# shelf = BookShelf(300)
# print(shelf)


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"<Book: {self.name}>"


class Bookshelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self):
        return f"<Bookshelf with {len(self.books)} books>"


book1 = Book("Harry Potter")
book2 = Book("Tersla")
bookshelf = Bookshelf([book1, book2])
print(bookshelf)
