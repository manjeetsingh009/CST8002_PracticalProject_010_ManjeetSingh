"""
Course: CST8002 – Programming Language Research Project
Professor: Stanley Pieda
Due Date: 29-03-2026
Author: Manjeet Singh
Student Number: 041160093

References:
[1] Python Software Foundation, "csv — CSV File Reading and Writing,"
https://docs.python.org/3/library/csv.html
[Accessed: Mar. 29, 2026].

[2] Python Software Foundation, "uuid — UUID Objects,"
https://docs.python.org/3/library/uuid.html
[Accessed: Mar. 29, 2026].

[3] Python Software Foundation, "list.sort() method,"
https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
[Accessed: Mar. 29, 2026].

[4] GeeksforGeeks, "Python List sort() Method," 
[Online]. Available: https://www.geeksforgeeks.org/python-list-sort-method/ 
[Accessed: Mar. 29, 2026].
"""

from model.shorebird_model import ShorebirdModel
from view.shorebird_view import ShorebirdView


class ShorebirdController:
    """Controller connecting Model and View."""

    def __init__(self, filepath):
        self.model = ShorebirdModel()
        self.view = ShorebirdView()
        self.filepath = filepath
        self.model.load_data(filepath)

    def run(self):
        while True:
            self.view.display_header()
            self.view.display_menu()
            choice = self.view.get_input()

            if choice == "1":
                self.view.display_records(self.model.records)

            elif choice == "2":
                year = input("Enter Site Identification: ")
                area = input("Enter Area: ")
                date = input("Enter Visit Date: ")
                time = input("Enter Start Time: ")
                species = input("Enter Species Code: ")
                count = input("Enter Count: ")

                self.model.add_record([year, area, date, time, species, count])
                self.view.show_message("Record added.")

            elif choice == "3":
                index = int(input("Enter record index to edit: "))
                if 0 <= index < len(self.model.records):
                    year = input("Enter Site Identification: ")
                    area = input("Enter Area: ")
                    date = input("Enter Visit Date: ")
                    time = input("Enter Start Time: ")
                    species = input("Enter Species Code: ")
                    count = input("Enter Count: ")

                    self.model.records[index] = [year, area, date, time, species, count]
                    self.view.show_message("Record updated.")

            elif choice == "4":
                index = int(input("Enter record index to delete: "))
                self.model.delete_record(index)
                self.view.show_message("Record deleted.")

            elif choice == "5":
                self.model.load_data(self.filepath)
                self.view.show_message("Dataset reloaded.")

            elif choice == "6":
                filename = self.model.save_data()
                self.view.show_message(f"Saved to {filename}")

            # ✅ SORTING FEATURE
            elif choice == "7":
                try:
                    print("\nSort by:")
                    print("1. Site Identification")
                    print("2. Area")
                    print("3. Visit Date")
                    print("4. Start Time")
                    print("5. Species Code")
                    print("6. Count")

                    field_choice = input("Choose field: ")

                    if field_choice == "1":
                        index = 0
                    elif field_choice == "2":
                        index = 1
                    elif field_choice == "3":
                        index = 2
                    elif field_choice == "4":
                        index = 3
                    elif field_choice == "5":
                        index = 4
                    elif field_choice == "6":
                        index = 5
                    else:
                        self.view.show_message("Invalid field.")
                        continue

                    print("\nSort order:")
                    print("1. Ascending")
                    print("2. Descending")
                    order = input("Choose order: ")

                    reverse = True if order == "2" else False

                    success = self.model.sort_records(index, reverse)

                    if success:
                        self.view.show_message("Records sorted successfully.")
                    else:
                        self.view.show_message("Sorting failed.")

                except Exception:
                    self.view.show_message("Error during sorting.")

            # ✅ FIXED OPTION 8 (DISPLAY MULTIPLE RECORDS)
            elif choice == "8":
                try:
                    number = int(input("Enter number of records to display: "))

                    # 🔥 DEBUG (optional – remove later)
                    print("TOTAL RECORDS LOADED:", len(self.model.records))

                    if number <= 0:
                        self.view.show_message("Enter a positive number.")
                        continue

                    # ✅ CORRECT FUNCTION CALL
                    self.view.display_multiple_records(self.model.records, number)

                except ValueError:
                    self.view.show_message("Invalid number.")

            elif choice == "9":
                break