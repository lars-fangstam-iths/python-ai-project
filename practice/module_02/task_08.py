from apartments import apartments

for apt in apartments:
    if apt["district"] == 'Angered':
        print(apt['listing_id'], apt['price'])