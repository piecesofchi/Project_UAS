class BookData:
    def _init_(self):
        self.books = []  # List untuk menyimpan data buku

    def add_book(self, title, author, year):
        self.books.append({"Title": title, "Author": author, "Year": year})

    def delete_book(self, title):
        for book in self.books:
            if book["Title"].lower() == title.lower():
                self.books.remove(book)
                return True
        return False

    def get_books(self):
        return self.books