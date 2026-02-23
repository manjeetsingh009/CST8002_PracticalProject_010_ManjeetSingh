"""
Course: CST8002 – Programming Language Research Project
Professor: Stanley Pieda
Due Date: 22-02-2026
Author: Manjeet Singh
Student Number: 041160093

References:
[1] Python Software Foundation, "Control Flow Tools,"
https://docs.python.org/3/tutorial/controlflow.html

[2] Python Software Foundation, "Exception Handling,"
https://docs.python.org/3/tutorial/errors.html

[3] Kirill Fakhroutdinov, "Multi-Layered Application: UML Model Diagram Example,"
https://www.uml-diagrams.org/multi-layered-application-uml-model-diagram-example.html
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
                year = input("Enter Year: ")
                name = input("Enter Bird Name: ")
                habitat = input("Enter Habitat: ")
                date = input("Enter Date: ")
                self.model.add_record([year, name, habitat, date])
                self.view.show_message("Record added.")

            elif choice == "3":
                index = int(input("Enter record index to edit: "))
                year = input("Enter new Year: ")
                name = input("Enter new Bird Name: ")
                habitat = input("Enter new Habitat: ")
                date = input("Enter new Date: ")
                if 0 <= index < len(self.model.records):
                    self.model.records[index] = [year, name, habitat, date]
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

            elif choice == "7":
                break