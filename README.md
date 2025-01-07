# Project_UAS

Program Manajemen Perpustakaan sederhana menggunakan konsep Modular dan OOP
Program ini memiliki tiga komponen utama


1. Class Data

'''python
 
    

Bertanggung jawab untuk menyimpan dan mengelola data buku yang ada di perpustakaan. Data ini disimpan dalam bentuk daftar yang terdiri dari leksikon, dengan judul, penulis, dan tahun       terbit untuk setiap buku.


2. Class View

'''python

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

Bertanggung jawab atas interaksi dengan pengguna; ia akan menampilkan daftar buku dalam bentuk tabel dan meminta input pengguna. Selain itu, ia juga bertanggung jawab untuk menampilkan   pesan ke pengguna, seperti konfirmasi atau kesalahan.


3. Class Process

'''python

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

Process Class digunakan untuk menghubungkan data dan tampilan. class ini memiliki logika untuk menambah buku ke dalam data dan menampilkan daftar buku. Proses akan menangani kesalahan jika ada data yang tidak valid atau salah.


Main Program

'''python

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

OUTPUT

![Capture](https://github.com/user-attachments/assets/899a75d0-ea76-41bb-ae0c-9c9a3fd55c8b)

