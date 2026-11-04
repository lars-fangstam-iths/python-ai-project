from apartments import apartments
from home import Home

homes = []
for apt in apartments:
    homes.append(Home(apt['listing_id'], apt['district'], int(apt['living_area']), int(apt['price'])))

print(len(homes))
print(homes[0])