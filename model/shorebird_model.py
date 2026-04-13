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

import csv
import uuid


class ShorebirdModel:
    """Model layer for data storage and file operations."""

    def __init__(self):
        self.records = []

    def load_data(self, filepath):
        """Load all records from dataset."""
        self.records.clear()
        with open(filepath, newline='', encoding='cp1252') as file:
            reader = csv.reader(file)

          

            for row in reader:   # ✅ load ALL records (no limit)
                self.records.append(row)

    def add_record(self, record):
        self.records.append(record)

    def delete_record(self, index):
        if 0 <= index < len(self.records):
            del self.records[index]

    def save_data(self):
        filename = f"shorebird_output_{uuid.uuid4()}.csv"
        with open(filename, 'w', newline='', encoding='cp1252') as file:
            writer = csv.writer(file)
            writer.writerows(self.records)
        return filename

    # ✅ SORTING FEATURE (OLD)
    def sort_records(self, index, reverse=False):
        """Sort records based on column index."""
        try:
            self.records.sort(
                key=lambda r: r[index].lower() if isinstance(r[index], str) else r[index],
                reverse=reverse
            )
            return True
        except Exception:
            return False

    # ✅ NEW FEATURE FOR PROJECT 4 (MULTI-COLUMN SORTING)
    def sort_records_multi(self, indices, reverse=False):
        """Sort records based on multiple column indices."""
        try:
            self.records.sort(
                key=lambda r: tuple(
                    r[i].lower() if isinstance(r[i], str) else r[i]
                    for i in indices
                ),
                reverse=reverse
            )
            return True
        except Exception:
            return False