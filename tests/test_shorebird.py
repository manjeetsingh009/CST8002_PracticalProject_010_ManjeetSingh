"""
Course: CST8002 – Programming Language Research Project
Professor: Stanley Pieda
Due Date: 22-02-2026
Author: Manjeet Singh
Student Number: 041160093

References:
[1] Python Software Foundation, "unittest — Unit testing framework,"
https://docs.python.org/3/library/unittest.html

[2] Python Software Foundation, "assert Methods,"
https://docs.python.org/3/library/unittest.html#assert-methods

[3] R. Oliveira, “GUID vs UUID vs ULID: Understanding Unique Identifiers,”
Medium, Jul. 31, 2024. [Online]. Available:
https://medium.com/@ronaldo.oliver7/guid-vs-uuid-vs-ulid-understanding-unique-identifiers-565c88cdca13
"""

import unittest
from model.shorebird_model import ShorebirdModel


class TestShorebird(unittest.TestCase):
    """Unit test for ShorebirdModel."""

    def test_add_record(self):
        """Test that add_record increases record count."""
        model = ShorebirdModel()
        initial_count = len(model.records)
        model.add_record(["1", "Test Bird"])
        self.assertEqual(len(model.records), initial_count + 1)


if __name__ == "__main__":
    print("Unit Test by Manjeet Singh (041160093)")
    unittest.main()