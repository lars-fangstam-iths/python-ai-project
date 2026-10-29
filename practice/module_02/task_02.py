from apartments import apartments

first = apartments[0]
price = int(first['price'])
sqm = int(first['living_area'])
price_per_sqm = price/sqm

print(f"Price per square meter = {price_per_sqm:.0f} SEK")