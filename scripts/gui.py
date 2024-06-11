import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style
from tkinter import ttk
from library import Library, create_member, borrow_book, return_book
from models import Member, Book


class LibraryGUI:
    def __init__(self, root, library):
        self.root = root
        self.library = library
        self.root.title("Library Management System")
        self.root.configure(bg="#DEF2F1")  # Χρήση χρώματος από το σχήμα

        # Προσαρμογή του στυλ
        style = Style(theme="solar")

        # Δημιουργία notebook
        self.notebook = ttk.Notebook(self.root)

        self.member_frame = ttk.Frame(self.notebook, style="Custom.TFrame")
        self.book_frame = ttk.Frame(self.notebook, style="Custom.TFrame")
        self.borrow_frame = ttk.Frame(self.notebook, style="Custom.TFrame")
        self.statistics_frame = ttk.Frame(self.notebook, style="Custom.TFrame")
        self.view_frame = ttk.Frame(self.notebook, style="Custom.TFrame")

        self.setup_member_frame()
        self.setup_book_frame()
        self.setup_borrow_frame()
        self.setup_statistics_frame()
        self.setup_view_frame()

        self.notebook.add(self.member_frame, text="Member Management")
        self.notebook.add(self.book_frame, text="Book Management")
        self.notebook.add(self.borrow_frame, text="Borrow/Return Books")
        self.notebook.add(self.statistics_frame, text="Statistics")
        self.notebook.add(self.view_frame, text="View Members & Books")
        self.notebook.pack(expand=1, fill="both")

    def setup_member_frame(self):
        self.member_frame.config(borderwidth=0, relief="flat")
        ttk.Label(
            self.member_frame, text="Member Management", style="Custom.TLabel"
        ).grid(row=0, columnspan=2, pady=10)

        # Member Form
        ttk.Label(self.member_frame, text="Member ID", style="Custom.TLabel").grid(
            row=1, column=0, padx=10, pady=5, sticky="e"
        )
        self.member_id_entry = ttk.Entry(self.member_frame, style="Custom.TEntry")
        self.member_id_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.member_frame, text="Name", style="Custom.TLabel").grid(
            row=2, column=0, padx=10, pady=5, sticky="e"
        )
        self.member_name_entry = ttk.Entry(self.member_frame, style="Custom.TEntry")
        self.member_name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.member_frame, text="Address", style="Custom.TLabel").grid(
            row=3, column=0, padx=10, pady=5, sticky="e"
        )
        self.member_address_entry = ttk.Entry(self.member_frame, style="Custom.TEntry")
        self.member_address_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.member_frame, text="Phone", style="Custom.TLabel").grid(
            row=4, column=0, padx=10, pady=5, sticky="e"
        )
        self.member_phone_entry = ttk.Entry(self.member_frame, style="Custom.TEntry")
        self.member_phone_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.member_frame, text="Email", style="Custom.TLabel").grid(
            row=5, column=0, padx=10, pady=5, sticky="e"
        )
        self.member_email_entry = ttk.Entry(self.member_frame, style="Custom.TEntry")
        self.member_email_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.member_frame, text="Age", style="Custom.TLabel").grid(
            row=6, column=0, padx=10, pady=5, sticky="e"
        )
        self.member_age_entry = ttk.Entry(self.member_frame, style="Custom.TEntry")
        self.member_age_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.member_frame, text="Profession", style="Custom.TLabel").grid(
            row=7, column=0, padx=10, pady=5, sticky="e"
        )
        self.member_profession_entry = ttk.Entry(
            self.member_frame, style="Custom.TEntry"
        )
        self.member_profession_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(
            self.member_frame, text="Membership Number", style="Custom.TLabel"
        ).grid(row=8, column=0, padx=10, pady=5, sticky="e")
        self.member_membership_number_entry = ttk.Entry(
            self.member_frame, style="Custom.TEntry"
        )
        self.member_membership_number_entry.grid(
            row=8, column=1, padx=10, pady=5, sticky="w"
        )

        self.member_create_button = ttk.Button(
            self.member_frame,
            text="Create Member",
            style="Custom.TButton",
            command=self.create_member,
        )
        self.member_create_button.grid(row=9, columnspan=2, pady=20)

    def create_member(self):
        member_id = self.member_id_entry.get()  # Λήψη τιμής από το πεδίο εισαγωγής
        name = self.member_name_entry.get()  # Λήψη τιμής από το πεδίο εισαγωγής
        address = self.member_address_entry.get()  # Λήψη τιμής από το πεδίο εισαγωγής
        phone = self.member_phone_entry.get()  # Λήψη τιμής από το πεδίο εισαγωγής
        email = self.member_email_entry.get()  # Λήψη τιμής από το πεδίο εισαγωγής
        age = self.member_age_entry.get()  # Λήψη τιμής από το πεδίο εισαγωγής
        profession = (
            self.member_profession_entry.get()
        )  # Λήψη τιμής από το πεδίο εισαγωγής
        membership_number = (
            self.member_membership_number_entry.get()
        )  # Λήψη τιμής από το πεδίο εισαγωγής

        member = create_member(
            self.library,
            member_id,
            name,
            address,
            phone,
            email,
            age,
            profession,
            membership_number,
        )
        messagebox.showinfo(
            "Success", f"Member {member.name} created successfully."
        )  # Εμφάνιση μηνύματος επιτυχίας

    def setup_book_frame(self):
        self.book_frame.config(borderwidth=0, relief="flat")
        ttk.Label(self.book_frame, text="Book Management", style="Custom.TLabel").grid(
            row=0, columnspan=2, pady=10
        )

        # Book Form
        ttk.Label(self.book_frame, text="Book ID", style="Custom.TLabel").grid(
            row=1, column=0, padx=10, pady=5, sticky="e"
        )
        self.book_id_entry = ttk.Entry(self.book_frame, style="Custom.TEntry")
        self.book_id_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.book_frame, text="Title", style="Custom.TLabel").grid(
            row=2, column=0, padx=10, pady=5, sticky="e"
        )
        self.book_title_entry = ttk.Entry(self.book_frame, style="Custom.TEntry")
        self.book_title_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.book_frame, text="Author", style="Custom.TLabel").grid(
            row=3, column=0, padx=10, pady=5, sticky="e"
        )
        self.book_author_entry = ttk.Entry(self.book_frame, style="Custom.TEntry")
        self.book_author_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.book_frame, text="Category", style="Custom.TLabel").grid(
            row=4, column=0, padx=10, pady=5, sticky="e"
        )
        self.book_category_entry = ttk.Entry(self.book_frame, style="Custom.TEntry")
        self.book_category_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.book_frame, text="ISBN", style="Custom.TLabel").grid(
            row=5, column=0, padx=10, pady=5, sticky="e"
        )
        self.book_isbn_entry = ttk.Entry(self.book_frame, style="Custom.TEntry")
        self.book_isbn_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.book_frame, text="Stock", style="Custom.TLabel").grid(
            row=6, column=0, padx=10, pady=5, sticky="e"
        )
        self.book_stock_entry = ttk.Entry(self.book_frame, style="Custom.TEntry")
        self.book_stock_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        self.book_create_button = ttk.Button(
            self.book_frame,
            text="Add Book",
            style="Custom.TButton",
            command=self.add_book,
        )
        self.book_create_button.grid(row=7, columnspan=2, pady=20)

    def add_book(self):
        book_id = self.book_id_entry.get()  # Λήψη τιμής από το πεδίο εισαγωγής
        title = self.book_title_entry.get()  # Λήψη τιμής από το πεδίο εισαγωγής
        author = self.book_author_entry.get()  # Λήψη τιμής από το πεδίο εισαγωγής
        category = self.book_category_entry.get()  # Λήψη τιμής από το πεδίο εισαγωγής
        isbn = self.book_isbn_entry.get()  # Λήψη τιμής από το πεδίο εισαγωγής
        stock = int(self.book_stock_entry.get())  # Λήψη τιμής από το πεδίο εισαγωγής

        book = Book(book_id, title, author, category, isbn, stock)
        self.library.add_book(book)
        messagebox.showinfo(
            "Success", f"Book {book.title} added successfully."
        )  # Εμφάνιση μηνύματος επιτυχίας

    def setup_borrow_frame(self):
        self.borrow_frame.config(borderwidth=0, relief="flat")
        ttk.Label(
            self.borrow_frame, text="Borrow/Return Books", style="Custom.TLabel"
        ).grid(row=0, columnspan=2, pady=10)

        # Borrow Form
        ttk.Label(self.borrow_frame, text="Member ID", style="Custom.TLabel").grid(
            row=1, column=0, padx=10, pady=5, sticky="e"
        )
        self.borrow_member_id_entry = ttk.Entry(
            self.borrow_frame, style="Custom.TEntry"
        )
        self.borrow_member_id_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.borrow_frame, text="Book ID", style="Custom.TLabel").grid(
            row=2, column=0, padx=10, pady=5, sticky="e"
        )
        self.borrow_book_id_entry = ttk.Entry(self.borrow_frame, style="Custom.TEntry")
        self.borrow_book_id_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.borrow_button = ttk.Button(
            self.borrow_frame,
            text="Borrow Book",
            style="Custom.TButton",
            command=self.borrow_book,
        )
        self.borrow_button.grid(row=3, columnspan=2, pady=20)

        self.return_button = ttk.Button(
            self.borrow_frame,
            text="Return Book",
            style="Custom.TButton",
            command=self.return_book,
        )
        self.return_button.grid(row=4, columnspan=2, pady=20)

    def borrow_book(self):
        member_id = (
            self.borrow_member_id_entry.get()
        )  # Λήψη τιμής από το πεδίο εισαγωγής
        book_id = self.borrow_book_id_entry.get()  # Λήψη τιμής από το πεδίο εισαγωγής

        if borrow_book(self.library, member_id, book_id):
            messagebox.showinfo(
                "Success", "Book borrowed successfully."
            )  # Εμφάνιση μηνύματος επιτυχίας
        else:
            messagebox.showerror(
                "Error", "Unable to borrow book."
            )  # Εμφάνιση μηνύματος σφάλματος

    def return_book(self):
        member_id = (
            self.borrow_member_id_entry.get()
        )  # Λήψη τιμής από το πεδίο εισαγωγής
        book_id = self.borrow_book_id_entry.get()  # Λήψη τιμής από το πεδίο εισαγωγής

        if return_book(self.library, member_id, book_id):
            messagebox.showinfo(
                "Success", "Book returned successfully."
            )  # Εμφάνιση μηνύματος επιτυχίας
        else:
            messagebox.showerror(
                "Error", "Unable to return book."
            )  # Εμφάνιση μηνύματος σφάλματος

    def setup_statistics_frame(self):
        self.statistics_frame.config(borderwidth=0, relief="flat")
        ttk.Label(self.statistics_frame, text="Statistics", style="Custom.TLabel").grid(
            row=0, columnspan=2, pady=10
        )

        self.stats_button = ttk.Button(
            self.statistics_frame,
            text="Show Statistics",
            style="Custom.TButton",
            command=self.show_statistics,
        )
        self.stats_button.grid(row=1, columnspan=2, pady=20)
        self.stats_text = tk.Text(
            self.statistics_frame,
            height=10,
            width=50,
            bg="#DEF2F1",
            fg="#17252A",
            font=("Helvetica", 12),
        )
        self.stats_text.grid(row=2, columnspan=2, pady=10)

    def show_statistics(self):
        stats = self.library.get_statistics()
        stats_text = f"Total Members: {stats['total_members']}\nTotal Books: {stats['total_books']}\nBorrowed Books: {stats['borrowed_books']}\n"
        self.stats_text.delete(1.0, tk.END)  # Καθαρισμός του πεδίου κειμένου
        self.stats_text.insert(tk.END, stats_text)  # Εισαγωγή των στατιστικών στοιχείων

    def setup_view_frame(self):
        self.view_frame.config(borderwidth=0, relief="flat")
        ttk.Label(
            self.view_frame, text="View Members & Books", style="Custom.TLabel"
        ).grid(row=0, columnspan=2, pady=10)

        self.view_button = ttk.Button(
            self.view_frame,
            text="Refresh View",
            style="Custom.TButton",
            command=self.refresh_view,
        )
        self.view_button.grid(row=1, columnspan=2, pady=20)
        self.view_text = tk.Text(
            self.view_frame,
            height=20,
            width=50,
            bg="#DEF2F1",
            fg="#17252A",
            font=("Helvetica", 12),
        )
        self.view_text.grid(row=2, columnspan=2, pady=10)

    def refresh_view(self):
        members = self.library.members
        books = self.library.books

        view_text = "Members:\n"
        for member in members.values():
            view_text += f"ID: {member.member_id}, Name: {member.name}, Borrowed Books: {[book_id for book_id, _ in member.borrowed_books]}\n"

        view_text += "\nBooks:\n"
        for book in books.values():
            view_text += (
                f"ID: {book.book_id}, Title: {book.title}, Stock: {book.stock}\n"
            )

        self.view_text.delete(1.0, tk.END)  # Καθαρισμός του πεδίου κειμένου
        self.view_text.insert(
            tk.END, view_text
        )  # Εισαγωγή των δεδομένων μελών και βιβλίων


if __name__ == "__main__":
    root = tk.Tk()
    style = Style(theme="solar")

    # Ορισμός custom στυλ
    style.configure(
        "Custom.TFrame",
        background="#3AAFA9",
    )
    style.configure(
        "Custom.TLabel",
        background="#DEF2F1",
        foreground="#17252A",
        font=("Helvetica", 12),
    )
    style.configure(
        "Custom.TEntry",
        fieldbackground="#FEFFFF",
        foreground="#17252A",
        font=("Helvetica", 12),
    )
    style.configure(
        "Custom.TButton",
        background="#3AAFA9",
        foreground="#FEFFFF",
        font=("Helvetica", 12),
        padding=10,
    )
    style.map(
        "Custom.TButton",
        background=[("active", "#2B7A78")],
    )

    library = Library()
    app = LibraryGUI(root, library)
    root.mainloop()
