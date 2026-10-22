"""Offline dictionary test on a user-owned, encrypted LibreOffice ODT.

Refactored from a classroom demonstration; run only with authorization.
Usage: python odt_dictionary_demo.py encrypted.odt wordlist.txt decrypted.odt
"""

import argparse
from pathlib import Path

from odfdecrypt import IncorrectPasswordError, decrypt, is_encrypted


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", type=Path, help="Encrypted ODT file you own")
    parser.add_argument("dictionary", type=Path, help="Newline-delimited test passwords")
    parser.add_argument("output", type=Path, help="Where to save decrypted output")
    args = parser.parse_args()

    if not args.document.is_file() or not args.dictionary.is_file():
        parser.error("The encrypted document and dictionary must both exist.")
    if args.output.exists():
        parser.error("Output file exists. Choose a new path to avoid overwriting it.")
    if args.output.resolve() == args.document.resolve():
        parser.error("Output must be separate from the evidence document.")
    if not is_encrypted(str(args.document)):
        parser.error("The specified ODT is not recognized as encrypted.")

    candidates = args.dictionary.read_text(encoding="utf-8-sig").splitlines()
    print(f"Loaded {len(candidates)} password candidates")

    for attempt, password in enumerate(candidates, start=1):
        print(f"Attempt {attempt}: testing candidate", flush=True)
        try:
            recovered = decrypt(str(args.document), password)
        except IncorrectPasswordError:
            continue
        args.output.write_bytes(recovered.getvalue())
        print(f"Password recovered on attempt {attempt}: {password}")
        print(f"Decrypted copy saved to {args.output}")
        return

    print("No password from the supplied dictionary matched.")


if __name__ == "__main__":
    main()
