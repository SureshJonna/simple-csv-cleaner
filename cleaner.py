import argparse
import csv
from pathlib import Path


def clean_csv(input_file, output_file):
    input_path = Path(input_file)
    output_path = Path(output_file)

    if input_path.resolve() == output_path.resolve():
        raise ValueError("Choose a different output file to protect the original.")

    cleaned_rows = []
    seen = set()
    removed = 0

    with input_path.open(newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        header = next(reader, None)

        if header is None:
            raise ValueError("The input file is empty.")

        header = [name.strip() for name in header]

        for row in reader:
            cleaned_row = [value.strip() for value in row]

            if not any(cleaned_row):
                removed += 1
                continue

            row_key = tuple(cleaned_row)

            if row_key in seen:
                removed += 1
                continue

            seen.add(row_key)
            cleaned_rows.append(cleaned_row)

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(cleaned_rows)

    return len(cleaned_rows), removed


def main():
    parser = argparse.ArgumentParser(description="Clean a CSV file.")
    parser.add_argument("input", help="CSV file to clean")
    parser.add_argument("output", help="Where to save the cleaned CSV")
    args = parser.parse_args()

    try:
        kept, removed = clean_csv(args.input, args.output)
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        parser.exit(1, f"Error: {error}\n")

    print(f"Done! Kept {kept} rows and removed {removed} rows.")
    print(f"Saved to: {args.output}")


if __name__ == "__main__":
    main()
