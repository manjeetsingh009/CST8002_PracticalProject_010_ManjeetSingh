"""
Course: CST8002 – Programming Language Research Project
Professor: Stanley Pieda
Due Date: 12-04-2026
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
[5] Government of Canada, “Open Government Licence – Canada,”
https://open.canada.ca/en/open-government-licence-canada (accessed Apr. 11, 2026).

"""

class ShorebirdView:

    def display_header(self):
        print("\n==================================================")
        print("CST8002 – Programming Language Research Project")
        print("Program by Manjeet Singh (041160093)")
        print("==================================================")

    def display_menu(self):
        print("\nPlease select an option:")
        print("1. Display Records")
        print("2. Add Record")
        print("3. Edit Record")
        print("4. Delete Record")
        print("5. Reload Dataset")
        print("6. Save Records (UUID)")
        print("7. Sort Records (Single)")
        print("8. Display Multiple Records")
        print("9. Sort Records (Multi-Column)")
        print("10. Exit")

    def get_input(self):
        return input("Choose option: ")

    # ✅ SAME (Option 1 → first 10 only)
    def display_records(self, records):
        for i, record in enumerate(records[:10]):
            print(i, record)

    # ✅ UPDATED (small addition for Project 4 clarity)
    def display_multiple_records(self, records, number):
        print("\nDisplaying records (after sorting if applied)...")  # 👈 ADDED LINE
        for i, record in enumerate(records[:number]):
            print(i, record)

    def show_message(self, message):
        print(message)