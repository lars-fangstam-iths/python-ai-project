from apartments import apartments

first = apartments[0]

print(first.get('balcony'))

print(first.get('balcony', 'unknown'))

print(first['balcony'])