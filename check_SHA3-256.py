"""
The program computes the SHA3-256 hash of a file 
and compares the hash with a missing value.

It works with Python 3.8+

If you have older version of Python3, you should install pysha3 package:
pip install pysha3
"""

import hashlib
from pathlib import Path

print()
print("===== WELCOME TO CHECK SHA3-256 PROGRAM =====")
print()

input_path = input("Type the path to your file:\n").strip()
try:
    print()
    print("Computing SHA3-256 hash...")
    path = Path(input_path)
    h = hashlib.sha3_256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    file_hash = str(h.hexdigest())
    print("Done!")
    missing_hash = input("\nType missing value:\n").strip()
    print()
    print("Comparing...")
    print("Done!")
    print()
    if file_hash == missing_hash:
        print("EVERYTHING IS OK.")
    else:
        print("WARNING: file hash does not match expected value — the file may be corrupted or tampered with.")
except Exception:
    print()
    print("Can not find the file. Is the path correct? Try again...")

print()
print("===== HAVE A NICE DAY. GOODBYE! =====")
print()
