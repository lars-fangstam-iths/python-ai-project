from apartments import apartments
from home import Home

class SavedSearch():
    def __init__(self, maximum_price, district):
        self.maximum_price = maximum_price
        self.district = district

    def matches(self, home):
        #return home.price <= self.maximum_price and home.district == self.district
        return home.is_within(self.maximum_price) and home.district == self.district

homes = []
for apt in apartments:
    homes.append(Home(apt['listing_id'], apt['district'], int(apt['living_area']), int(apt['price'])))

search = SavedSearch(2_200_000, 'Angered')

for home in homes:
    if search.matches(home):
        print(home)