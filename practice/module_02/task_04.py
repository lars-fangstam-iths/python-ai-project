from apartments import apartments

last1 = apartments[-1]
print(f"{last1['listing_id']}: {last1['price']}")

last2 = apartments[len(apartments) -1]
print(f"{last2['listing_id']}: {last2['price']}")