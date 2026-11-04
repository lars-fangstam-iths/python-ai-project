import csv
from pathlib import Path

def read_file(file_path):
    with open(path, encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))

def price_per_sqm(apt):
    return apt['price'] // apt['living_area'] # // = return int

path = Path("practice") / "data" / "apartments_small.csv"
apts = read_file(path)

print("Number of apartments: ", end="") # No newline.
print(len(apts))
print(f"Number of apartments: {len(apts)}")
print(f"Example row: {apts[0]}")

first_apt = apts[0]
first_apt['price'] = int(first_apt['price'])
first_apt['living_area'] = int(first_apt['living_area'])
print(f"Price per square meter: {price_per_sqm(apts[0]):,.0f}")
print(f"Price per square meter: {price_per_sqm(first_apt):,.0f}")
print(f"Price per square meter: {price_per_sqm(apts[0])}")
print(f"Price per square meter: {price_per_sqm(first_apt)}")

print(5 ** 2) # power of...

