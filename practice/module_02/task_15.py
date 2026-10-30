import csv
from pathlib import Path

path = Path('practice') / 'data' / 'apartments_small.csv'

print(path)

with open(path, encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))

print(len(rows))
print(rows[0])