"""
Course: CST8002 – Programming Language Research Project
Professor: Stanley Pieda
Due Date: 22-02-2026
Author: Manjeet Singh
Student Number: 041160093

References:
[1] Python Software Foundation, "csv — CSV File Reading and Writing,"
https://docs.python.org/3/library/csv.html

[2] Python Software Foundation, "uuid — UUID Objects,"
https://docs.python.org/3/library/uuid.html

[3] R. Oliveira, “GUID vs UUID vs ULID: Understanding Unique Identifiers,”
Medium, Jul. 31, 2024. [Online]. Available:
https://medium.com/@ronaldo.oliver7/guid-vs-uuid-vs-ulid-understanding-unique-identifiers-565c88cdca13
"""

import csv
import uuid


class ShorebirdModel:
    """Model layer for data storage and file operations."""

    def __init__(self):
        self.records = []

    def load_data(self, filepath):
        """Load up to 100 records from dataset."""
        self.records.clear()
        with open(filepath, newline='', encoding='cp1252') as file:
            reader = csv.reader(file)
            next(reader)
            next(reader)
            for i, row in enumerate(reader):
                if i >= 100:
                    break
                self.records.append(row)

    def add_record(self, record):
        """Add record to memory."""
        self.records.append(record)

    def delete_record(self, index):
        """Delete record by index."""
        if 0 <= index < len(self.records):
            del self.records[index]

    def save_data(self):
        """Save records to new CSV file using UUID."""
        filename = f"shorebird_output_{uuid.uuid4()}.csv"
        with open(filename, 'w', newline='', encoding='cp1252') as file:
            writer = csv.writer(file)
            writer.writerows(self.records)
        return filename