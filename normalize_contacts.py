"""Normalize names and email addresses in a CSV file."""

import argparse
import csv
import unicodedata
from pathlib import Path


def normalize_text(value):
    """Apply Unicode compatibility normalization and collapse whitespace."""
    return " ".join(unicodedata.normalize("NFKC", value).split())


def normalize_contacts(input_path, output_path):
    """Normalize name and email columns from an input CSV into an output CSV."""
    input_file = Path(input_path)
    output_file = Path(output_path)
    if input_file.resolve() == output_file.resolve():
        raise ValueError("Input and output paths must be different.")

    with input_file.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        if not reader.fieldnames:
            raise ValueError("The input CSV must include a header row.")

        headers = {}
        for header in reader.fieldnames:
            normalized_header = header.strip().casefold()
            if normalized_header in ("name", "email"):
                if normalized_header in headers:
                    raise ValueError(
                        f"The input CSV contains multiple {normalized_header!r} columns."
                    )
                headers[normalized_header] = header

        missing_headers = {"name", "email"} - headers.keys()
        if missing_headers:
            missing = ", ".join(sorted(missing_headers))
            raise ValueError(f"The input CSV is missing required column(s): {missing}.")

        with output_file.open("w", encoding="utf-8", newline="") as destination:
            writer = csv.DictWriter(destination, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row_number, row in enumerate(reader, start=2):
                if None in row:
                    raise ValueError(
                        f"CSV row {row_number} has more values than the header."
                    )
                for field in headers.values():
                    value = row[field]
                    if value is None:
                        raise ValueError(
                            f"CSV row {row_number} is missing a value for {field!r}."
                        )
                    row[field] = normalize_text(value)

                email_field = headers["email"]
                row[email_field] = row[email_field].lower()
                writer.writerow(row)


def main():
    """Parse command-line arguments and normalize the requested CSV file."""
    parser = argparse.ArgumentParser(
        description="Normalize name whitespace and lowercase email addresses in a CSV."
    )
    parser.add_argument("input_csv", help="CSV file with name and email columns")
    parser.add_argument("output_csv", help="Path for the normalized CSV output")
    args = parser.parse_args()

    try:
        normalize_contacts(args.input_csv, args.output_csv)
    except (OSError, ValueError, csv.Error) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
