from apartments import apartments

listed = [round(apartment['price'] / apartment['living_area']) for apartment in apartments]

print(listed)