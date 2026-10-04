# Simple CSV Cleaner

A small Python tool that cleans CSV files without extra packages.

This is a beginner learning project. It is intended for simple,
comma-separated files with a header row.

## Features

- Removes spaces from the start and end of each cell.
- Removes rows where every cell is empty.
- Removes duplicate data rows after cleaning spaces.
- Keeps the first copy of each duplicate row.
- Saves the result to a separate file.
- Rejects using the same path for input and output.

## Requirements

Python 3.12 is used in the automated tests.

No extra Python packages are needed.

## Get the project

On the repository page, select Code → Download ZIP.

Extract the ZIP, then open a terminal inside the extracted folder.

## Try the example

Run:

```bash
python cleaner.py examples/sample.csv cleaned.csv
```

On Windows, if the `python` command is not available, try:

```bash
py cleaner.py examples/sample.csv cleaned.csv
```

Expected message for the included sample:

```text
Done! Kept 3 rows and removed 2 rows.
Saved to: cleaned.csv
```

Open `cleaned.csv` to see the result.

## Clean your own file

Copy your CSV into the project folder, then run:

```bash
python cleaner.py your_file.csv your_file_cleaned.csv
```

Use a new output filename. An existing output file will be overwritten.

Keep a backup of important data.

## Run tests

```bash
python -m unittest discover -s tests -v
```

GitHub Actions also runs the tests on pushes and pull requests.

## Limits

- Supports comma-separated CSV files, not Excel `.xlsx` files.
- Expects UTF-8 text, with or without a byte-order mark.
- Treats the first row as column names.
- Duplicate matching is case-sensitive.
- Does not validate email addresses or repair incorrect values.
- Does not check that every row has the same number of columns.
- Removes surrounding spaces even when they are intentional.

## Privacy

The script does not send data over the internet.

Do not upload private or sensitive CSV files to this public repository.
Use fictional data in examples and bug reports.

## Contributions

Suggestions, bug reports, and small improvements are welcome.

Please explain the problem and include a small fictional example.

## Project status

This is a new learning project. No claims of wide adoption or
established community impact are made.

## License

MIT License. See LICENSE for details.
