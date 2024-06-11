from collections import defaultdict
import datetime
from models import Member, Book


class Library:
    def __init__(self):
        self.members = {}  # Λεξικό για αποθήκευση μελών
        self.books = {}  # Λεξικό για αποθήκευση βιβλίων
        self.categories = defaultdict(list)  # Λεξικό κατηγοριών με λίστες βιβλίων

    def add_member(self, member):
        self.members[member.member_id] = member  # Προσθήκη μέλους στο λεξικό

    def add_book(self, book):
        self.books[book.book_id] = book  # Προσθήκη βιβλίου στο λεξικό
        self.categories[book.category].append(
            book
        )  # Προσθήκη βιβλίου στην κατηγορία του

    def borrow_book(self, member_id, book_id):
        member = self.members.get(member_id)  # Αναζήτηση μέλους
        book = self.books.get(book_id)  # Αναζήτηση βιβλίου
        if book and member and book.stock > 0:  # Έλεγχος διαθεσιμότητας
            book.stock -= 1  # Μείωση αποθέματος βιβλίου
            member.borrowed_books.append(
                (book_id, datetime.date.today())
            )  # Προσθήκη βιβλίου στη λίστα δανεισμένων βιβλίων του μέλους
            return True
        return False

    def return_book(self, member_id, book_id):
        member = self.members.get(member_id)  # Αναζήτηση μέλους
        book = self.books.get(book_id)  # Αναζήτηση βιβλίου
        if (
            book
            and member
            and any(
                book_id == borrowed_book[0] for borrowed_book in member.borrowed_books
            )
        ):
            book.stock += 1  # Αύξηση αποθέματος βιβλίου
            member.borrowed_books = [
                borrowed_book
                for borrowed_book in member.borrowed_books
                if borrowed_book[0] != book_id
            ]  # Αφαίρεση βιβλίου από τη λίστα δανεισμένων βιβλίων του μέλους
            return True
        return False

    def get_available_books(self, category=None):
        if category:
            return [
                book for book in self.categories.get(category, []) if book.stock > 0
            ]  # Λίστα διαθέσιμων βιβλίων σε συγκεκριμένη κατηγορία
        return [
            book for book in self.books.values() if book.stock > 0
        ]  # Λίστα διαθέσιμων βιβλίων

    def get_statistics(self):
        stats = {
            "total_members": len(self.members),  # Σύνολο μελών
            "total_books": len(self.books),  # Σύνολο βιβλίων
            "borrowed_books": sum(
                len(member.borrowed_books) for member in self.members.values()
            ),  # Σύνολο δανεισμένων βιβλίων
        }
        return stats


def create_member(
    library, member_id, name, address, phone, email, age, profession, membership_number
):
    member = Member(
        member_id, name, address, phone, email, age, profession, membership_number
    )  # Δημιουργία νέου μέλους
    library.add_member(member)  # Προσθήκη μέλους στη βιβλιοθήκη
    return member


def update_member(library, member_id, **kwargs):
    member = library.members.get(member_id)  # Αναζήτηση μέλους
    if member:
        member.update_info(**kwargs)  # Ενημέρωση στοιχείων μέλους
        return member
    return None


def delete_member(library, member_id):
    if member_id in library.members:
        del library.members[member_id]  # Διαγραφή μέλους
        return True
    return False


def borrow_book(library, member_id, book_id):
    return library.borrow_book(member_id, book_id)  # Δανεισμός βιβλίου


def return_book(library, member_id, book_id):
    return library.return_book(member_id, book_id)  # Επιστροφή βιβλίου
