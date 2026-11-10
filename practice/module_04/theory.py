class EstateAgent:
    def __init__(self, name, phone, sales=0):
        self.name = name
        self.phone = phone
        self.sales = sales

    def __repr__(self):
        return (
            f"EstateAgent(name={self.name!r}, "
            f"phone={self.phone!r}, sales={self.sales})"
        )

    def __eq__(self, other):
        if not isinstance(other, EstateAgent):
            return False
        return (self.name, self.phone, self.sales) == (other.name, other.phone, other.sales)


kim = EstateAgent("Kim", "031-390 06 00")
same = EstateAgent("Kim", "031-390 06 00")

# print(kim)
# print(kim == same)


class Commission:
    def __init__(self, rate):
        self.rate = rate

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        if not 0 <= value <= 0.1:
            raise ValueError(f"rate must be between 0 and 0.1, not {value}")
        self._rate = value


commission = Commission(0.03)
print(commission.rate)
commission.rate = 0.5