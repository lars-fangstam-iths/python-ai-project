from dataclasses import dataclass

@dataclass
class Home:
    listing_id: str
    district: str
    living_area: int
    price: int
    elevator: str = "unknown"

    def price_per_sqm(self):
        return round(self.price / self.living_area)

@dataclass(frozen=True)
class Location:
    latitude: float
    longitude: float

@dataclass
class EstateAgent:
    name: str
    phone: str

@dataclass
class Listing:
    home: Home
    agent: EstateAgent
    asking_price: int

    def describe(self):
        return f"{self.home.listing_id} in {self.home.district}, {self.asking_price:,} SEK, call {self.agent.name} on {self.agent.phone}."

class ListingClass():
    _price_per_sqm: int

    def __init__(self, home: Home, agent: EstateAgent, asking_price: int):
        self.home = home
        self.agent = agent
        self.asking_price = asking_price
        self._price_per_sqm = asking_price // home.living_area

    # Public property that controls access
    @property
    def asking_price(self):
        return self._asking_price # Private attribute that stores the actual value

    @asking_price.setter
    def asking_price(self, value):
        if value < 0:
            raise ValueError("Asking price can not be a negative value!")
        self._asking_price = value

    # Only a getter, no setter.
    @property
    def price_per_sqm(self):
        return round(self.asking_price / self.home.living_area)

    def describe(self):
            # Reads self.asking_price, which now goes through the property.
            return f"{self.home.listing_id} in {self.home.district}, {self.asking_price:,} SEK, call {self.agent.name} on {self.agent.phone}."
