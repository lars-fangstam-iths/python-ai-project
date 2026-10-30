import csv
from pathlib import Path
from collections import Counter

path = Path('practice') / 'data' / 'apartments_small.csv'

with open(path, encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))

listed = [row['district'] for row in rows]
print(listed)

counted_districts = Counter([row['district'] for row in rows])
print('\n', counted_districts, '\n')

common = counted_districts.most_common()
print(common, '\n')

for district, count in counted_districts.most_common():
    print(district, count)