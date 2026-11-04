from apartments import apartments
from home import Home

homes = []
for apt in apartments:
    homes.append(Home(apt['listing_id'], apt['district'], int(apt['living_area']), int(apt['price'])))

homes_per_district = {}
for home in homes:
    homes_per_district[home.district] = homes_per_district.get(home.district, 0) + 1

print(homes_per_district)