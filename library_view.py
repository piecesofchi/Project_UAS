from tabulate import tabulate

class LibraryView:
    @staticmethod
    def display_books(books):
        if books:
            print(tabulate(books, headers="keys", tablefmt="grid"))
        else:
            print("Tidak ada buku di perpustakaan.")

    @staticmethod
    def show_message(message):
        print(message)