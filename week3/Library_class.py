class Library:
    def __init__(self):
        self.book = []  # create list once

    def add_book(self, name):
        self.book.append(name)

    def show_books(self):
        print("titles:")
        print(self.book)


book = Library()     
book.add_book("atomic habit")
book.add_book("the subtle art of .....")
book.add_book("Elements")
book.show_books()
