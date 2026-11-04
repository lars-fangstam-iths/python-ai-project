from apartments import apartments
from home import Home

homes = []
for apt in apartments:
    homes.append(Home(apt['listing_id'], apt['district'], int(apt['living_area']), int(apt['price'])))

homes.sort(key=lambda home: home.price_per_sqm())

for home in homes[:3]:
    print(home, home.price_per_sqm())