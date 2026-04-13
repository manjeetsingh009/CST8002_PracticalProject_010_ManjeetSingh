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