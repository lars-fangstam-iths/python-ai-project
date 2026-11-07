from home import Home


class Search:
    def __init__(self, max_price):
        self.max_price = max_price

    def matches(self, home):
        return home.price <= self.max_price


a06 = Home("A06", "Angered", 67, 1_481_000)
search = Search(2_000_000)
print(search.matches(a06))