from apartments import apartments
from home import Home

homes = []
for apt in apartments:
    homes.append(Home(apt['listing_id'], apt['district'], int(apt['living_area']), int(apt['price'])))

for home in homes:
    if home.is_within(2_000_000):
        print(home)