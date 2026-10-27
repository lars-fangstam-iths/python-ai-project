import csv
from pathlib import Path

path = Path("practice") / "data" / "apartments_small.csv"
with open(path, encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))

print(rows)
print(path)
print(type(path))
print(rows[0]["district"], rows[0]["price"])