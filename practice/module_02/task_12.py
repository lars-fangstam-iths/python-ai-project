from apartments import apartments

def price_sqm(price, sqm):
    return round(price / sqm)

first = apartments[0]
cost_sqm = price_sqm(first['price'], first['living_area'])

print(cost_sqm)
print(type(cost_sqm))
assert cost_sqm == round(apartments[0]['price'] / apartments[0]['living_area'])

listed = [round(apartment['price'] / apartment['living_area']) for apartment in apartments]

print(listed)