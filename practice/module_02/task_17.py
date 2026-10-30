import csv
import json
from pathlib import Path

load_path = Path('practice') / 'data' / 'apartments_small.csv'

with open(load_path, encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))

affordable = []
for apt in rows:
    if int(apt['price']) <= 2_000_000:
        affordable.append(apt)
# or:
affordable = [apt for apt in rows if int(apt['price']) <= 2_000_000]

print(len(affordable))

aff_json = json.dumps(affordable, ensure_ascii = False, indent = 2)
#print(aff_json)

save_path = Path('practice') / 'data' / 'affordable.json'

save_path.write_text(aff_json, encoding="utf-8")