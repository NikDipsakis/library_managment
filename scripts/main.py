from gui import LibraryGUI
from library import Library
import tkinter as tk

# Κύρια συνάρτηση για την εκτέλεση της εφαρμογής
if __name__ == "__main__":
    root = tk.Tk()  # Δημιουργία κύριου παραθύρου Tkinter
    library = Library()  # Δημιουργία αντικειμένου βιβλιοθήκης
    app = LibraryGUI(root, library)  # Δημιουργία του GUI και σύνδεση με τη βιβλιοθήκη
    root.mainloop()  # Εκκίνηση του κύριου βρόχου της εφαρμογής
