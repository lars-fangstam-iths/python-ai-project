class Home():
    def __init__(self, listing_id, district, living_area, price):
        if living_area <= 0:
            raise ValueError("Living area must be larger than 0!")

        if price < 0:
            raise ValueError("Price can not be a negative number!")
        
        self.listing_id = listing_id
        self.district = district
        self.living_area = living_area
        self.price = price

    def __repr__(self):
        return f"Home: ({self.listing_id!r}, {self.district!r}, {self.living_area}, {self.price})"
    
    def price_per_sqm(self):
        #return self.price // self.living_area
        return round(self.price / self.living_area)

    def is_within(self, budget):
        return self.price <= budget

    def lower_price(self, amount):
        if amount > self.price:
            raise ValueError("Can not lower the price to less than 0!")

        self.price -= amount
