import csv
import tempfile
import unittest
from pathlib import Path

from cleaner import clean_csv


class TestCleaner(unittest.TestCase):
    def test_cleaning(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "input.csv"
            destination = Path(folder) / "output.csv"

            original = (
                " name , city \n"
                " Suresh , Bengaluru \n"
                "Suresh,Bengaluru\n"
                ",\n"
                "Anita, Mysuru \n"
            )
            source.write_text(original, encoding="utf-8")

            kept, removed = clean_csv(source, destination)

            with destination.open(
                newline="", encoding="utf-8"
            ) as file:
                result = list(csv.reader(file))

            self.assertEqual(
                result,
                [
                    ["name", "city"],
                    ["Suresh", "Bengaluru"],
                    ["Anita", "Mysuru"],
                ],
            )
            self.assertEqual(kept, 2)
            self.assertEqual(removed, 2)
            self.assertEqual(
                source.read_text(encoding="utf-8"), original
            )

    def test_same_file_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "input.csv"
            source.write_text("name\nSuresh\n", encoding="utf-8")

            with self.assertRaises(ValueError):
                clean_csv(source, source)


if __name__ == "__main__":
    unittest.main()
