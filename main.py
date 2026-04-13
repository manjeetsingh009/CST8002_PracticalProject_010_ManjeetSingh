"""
Course: CST8002 – Programming Language Research Project
Professor: Stanley Pieda
Due Date: 12-04-2026
Author: Manjeet Singh
Student Number: 041160093
Description: Main entry point for MVC application.

References:
[1] Python Software Foundation, "csv — CSV File Reading and Writing,"
https://docs.python.org/3/library/csv.html

[2] Python Software Foundation, "uuid — UUID Objects,"
https://docs.python.org/3/library/uuid.html

[3] R. Oliveira, “GUID vs UUID vs ULID: Understanding Unique Identifiers,”
Medium, Jul. 31, 2024. [Online]. Available:
https://medium.com/@ronaldo.oliver7/guid-vs-uuid-vs-ulid-understanding-unique-identifiers-565c88cdca13
"""

from controller.shorebird_controller import ShorebirdController

DATASET_PATH = "data/pacific_rim_npr_coastalmarine_migratory_shorebird_habitat_use_2011-2017_data.csv"

if __name__ == "__main__":
    controller = ShorebirdController(DATASET_PATH)
    controller.run()