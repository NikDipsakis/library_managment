class Member:
    def __init__(
        self, member_id, name, address, phone, email, age, profession, membership_number
    ):
        self.member_id = member_id  # Μοναδικό αναγνωριστικό μέλους
        self.name = name  # Όνομα μέλους
        self.address = address  # Διεύθυνση μέλους
        self.phone = phone  # Τηλέφωνο μέλους
        self.email = email  # Email μέλους
        self.age = age  # Ηλικία μέλους
        self.profession = profession  # Επάγγελμα μέλους
        self.membership_number = membership_number  # Αριθμός μέλους
        self.borrowed_books = []  # Λίστα δανεισμένων βιβλίων

    def update_info(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)  # Ενημέρωση στοιχείων μέλους


class Book:
    def __init__(self, book_id, title, author, category, isbn, stock):
        self.book_id = book_id  # Μοναδικό αναγνωριστικό βιβλίου
        self.title = title  # Τίτλος βιβλίου
        self.author = author  # Συγγραφέας βιβλίου
        self.category = category  # Κατηγορία βιβλίου
        self.isbn = isbn  # ISBN βιβλίου
        self.stock = stock  # Απόθεμα βιβλίου
