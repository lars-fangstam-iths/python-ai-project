class EstateAgent:
    def __init__(self, name, district):
        self.name = name
        self.district = district
        self.sales = []

    def add_sale(self, price):
        if price <= 0:
            raise ValueError(f"a sale must be more than 0, not {price}")
        self.sales.append(price)


kim = EstateAgent("Kim", "Majorna")
print(kim)
kim.add_sale(0)