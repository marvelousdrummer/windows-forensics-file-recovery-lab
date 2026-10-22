"""Offline four-digit numeric password demonstration on a user-owned PDF.

Refactored from a classroom demonstration; run only with authorization.
Usage: python pdf_numeric_bruteforce_demo.py encrypted.pdf
"""

import argparse
import time
from pathlib import Path

from pypdf import PdfReader


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", type=Path, help="Encrypted PDF file you own")
    args = parser.parse_args()

    if not args.document.is_file():
        parser.error("The PDF file does not exist.")

    reader = PdfReader(str(args.document))
    if not reader.is_encrypted:
        parser.error("The PDF does not appear to be encrypted.")

    started = time.perf_counter()
    for number in range(10_000):
        password = f"{number:04d}"
        if number % 100 == 0:
            print(f"Testing {password}", flush=True)
        if reader.decrypt(password):
            print(f"Password recovered: {password}")
            print(f"Attempts: {number + 1}")
            print(f"Elapsed time: {time.perf_counter() - started:.2f} seconds")
            return
    print("No four-digit numeric password matched.")


if __name__ == "__main__":
    main()
