from dataclasses import dataclass
from listings import EstateAgent, Home, ListingClass

@dataclass
class Viewing:
    listing_id: str
    visitors: int


class Bid:
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value


viewing = Viewing("A01", 12)
listing = ListingClass(Home("A01", "Majorna", 50, 2_453_000), EstateAgent("Kim", "031-390 06 00"), 2_495_000)
print(viewing.visitors, listing.home.district)

bid = Bid(2_500_000)
bid.amount = 2_600_000
print(bid.amount)