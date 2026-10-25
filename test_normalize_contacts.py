import csv
import tempfile
import unittest
from pathlib import Path

from normalize_contacts import normalize_contacts, normalize_text


class TestNormalizeContacts(unittest.TestCase):
    def test_normalize_text_collapses_whitespace_and_normalizes_unicode(self):
        self.assertEqual(normalize_text("  Ａda\t  Lovelace \n"), "Ada Lovelace")

    def test_normalize_contacts_writes_normalized_csv(self):
        with tempfile.TemporaryDirectory() as directory:
            input_path = Path(directory) / "contacts.csv"
            output_path = Path(directory) / "normalized.csv"
            input_path.write_text(
                "Name,Email,Note\n  Ada   Lovelace , ADA@EXAMPLE.COM ,Keep This\n",
                encoding="utf-8",
            )

            normalize_contacts(input_path, output_path)

            with output_path.open(encoding="utf-8", newline="") as output_file:
                rows = list(csv.DictReader(output_file))
            self.assertEqual(
                rows,
                [
                    {
                        "Name": "Ada Lovelace",
                        "Email": "ada@example.com",
                        "Note": "Keep This",
                    }
                ],
            )

    def test_normalize_contacts_rejects_missing_columns(self):
        with tempfile.TemporaryDirectory() as directory:
            input_path = Path(directory) / "contacts.csv"
            output_path = Path(directory) / "normalized.csv"
            input_path.write_text("Name\nAda Lovelace\n", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "email"):
                normalize_contacts(input_path, output_path)

    def test_normalize_contacts_rejects_same_input_and_output_path(self):
        with tempfile.TemporaryDirectory() as directory:
            input_path = Path(directory) / "contacts.csv"
            input_path.write_text("Name,Email\nAda,ada@example.com\n", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "different"):
                normalize_contacts(input_path, input_path)


if __name__ == "__main__":
    unittest.main()
