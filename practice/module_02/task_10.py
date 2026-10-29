from apartments import apartments

cheapest = apartments[0]

for apt in apartments:
    if apt['price'] < cheapest['price']:
        cheapest = apt

print("Cheapest:", cheapest['listing_id'], cheapest['district'], cheapest['price'])