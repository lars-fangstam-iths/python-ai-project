import csv
from pathlib import Path

path = Path("practice") / "data" / "apartments_small.csv"
with open(path, encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))

cheap = [row for row in rows if int(row["price"]) <= 1_000_000]
for row in cheap:
    print(row["listing_id"], row["price"])

print(len(cheap), "cheap apartments")