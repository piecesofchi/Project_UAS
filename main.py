from book_data import BookData
from library_view import LibraryView
from library_process import LibraryProcess

def main():
    data = BookData()
    view = LibraryView()
    process = LibraryProcess(data, view)

    while True:
        print("\n=== Manajemen Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Hapus Buku")
        print("3. Lihat Buku")
        print("4. Keluar")
        choice = input("Pilih menu: ").strip()

        if choice == "1":
            process.add_book_process()
        elif choice == "2":
            process.delete_book_process()
        elif choice == "3":
            process.display_books_process()
        elif choice == "4":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            view.show_message("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
