class Data:
    def __init__(self):  # Corrected __init__ method
        self.books = []

    def add_book(self, title, author, year):
        self.books.append({"title": title, "author": author, "year": year})

    def get_books(self):
        return self.books


class View:
    def display_books(self, books):
        if len(books) == 0:
            print("Tidak ada buku dalam perpustakaan.")
        else:
            print(f"{'No':<5}{'Title':<30}{'Author':<30}{'Year':<10}")
            for index, book in enumerate(books, 1):
                print(f"{index:<5}{book['title']:<30}{book['author']:<30}{book['year']:<10}")

    def display_message(self, message):
        print(message)

    def get_input(self, prompt):
        return input(prompt)


class Process:
    def __init__(self, data, view):  # Corrected __init__ method
        self.data = data
        self.view = view

    def add_book(self):
        try:
            title = self.view.get_input("Masukkan judul buku: ")
            author = self.view.get_input("Masukkan nama penulis: ")
            year = int(self.view.get_input("Masukkan tahun terbit: "))
            self.data.add_book(title, author, year)
            self.view.display_message("Buku berhasil ditambahkan.")
        except ValueError:
            self.view.display_message("Tahun terbit harus berupa angka!")

    def show_books(self):
        books = self.data.get_books()
        self.view.display_books(books)


def main():
    data = Data()
    view = View()
    process = Process(data, view)

    while True:
        print("\n--- Menu Perpustakaan ---")
        print("1. Tambah Buku")
        print("2. Tampilkan Buku")
        print("3. Keluar")
        choice = input("Pilih menu (1/2/3): ")

        if choice == "1":
            process.add_book()
        elif choice == "2":
            process.show_books()
        elif choice == "3":
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":  # Corrected if condition
    main()
