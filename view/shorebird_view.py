"""
Course: CST8002 – Programming Language Research Project
Professor: Stanley Pieda
Due Date: 22-02-2026
Author: Manjeet Singh
Student Number: 041160093

References:
[1] Python Software Foundation, "print() function,"
https://docs.python.org/3/library/functions.html#print

[2] Python Software Foundation, "input() function,"
https://docs.python.org/3/library/functions.html#input

[3] R. Oliveira, “GUID vs UUID vs ULID: Understanding Unique Identifiers,”
Medium, Jul. 31, 2024. [Online]. Available:
https://medium.com/@ronaldo.oliver7/guid-vs-uuid-vs-ulid-understanding-unique-identifiers-565c88cdca13
"""


class ShorebirdView:
    """View layer handling user interaction."""

    def display_header(self):
        """Display program header."""
        print("\n==================================================")
        print("CST8002 – Programming Language Research Project")
        print("Program by Manjeet Singh (041160093)")
        print("==================================================")

    def display_menu(self):
        """Display menu options."""
        print("\nPlease select an option:")
        print("1. Display Records")
        print("2. Add Record")
        print("3. Edit Record")
        print("4. Delete Record")
        print("5. Reload Dataset")
        print("6. Save Records (UUID)")
        print("7. Exit")

    def get_input(self):
        return input("Choose option: ")

    def display_records(self, records):
        for i, record in enumerate(records[:10]):
            print(i, record)

    def show_message(self, message):
        print(message)