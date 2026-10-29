from statistics import median
from apartments import apartments

my_apartments = [
    { id: 0, 'price': 1_000_000 },
    { id: 0, 'price': 2_000_000 },
    { id: 0, 'price': 3_000_000 },
]

def median_price(apts):
    return median(apt['price'] for apt in apts)

print(median_price(my_apartments))
assert median_price(my_apartments) == 2000000

print(f"{median_price(apartments):,.0f}")
