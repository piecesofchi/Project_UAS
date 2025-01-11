class LibraryProcess:
    def _init_(self, data, view):
        self.data = data
        self.view = view

    def add_book_process(self):
        try:
            title = input("Masukkan judul buku: ").strip()
            if not title:
                raise ValueError("Judul buku tidak boleh kosong.")
            author = input("Masukkan penulis buku: ").strip()
            if not author:
                raise ValueError("Penulis buku tidak boleh kosong.")
            year = int(input("Masukkan tahun terbit : "))
            if year < 0:
                raise ValueError("Tahun terbit tidak valid.")
            self.data.add_book(title, author, year)
            self.view.show_message("Buku berhasil ditambahkan!")
        except ValueError as e:
            self.view.show_message(f"Kesalahan input: {e}")

    def delete_book_process(self):
        title = input("Masukkan judul buku yang ingin dihapus: ").strip()
        if self.data.delete_book(title):
            self.view.show_message("Buku berhasil dihapus!")
        else:
            self.view.show_message("Buku tidak ditemukan.")

    def display_books_process(self):
        books = self.data.get_books()
        self.view.display_books(books)
