class Home:
    def __init__(
            self,
            rooms: int,
            district: str,
            price: int,
    ) -> None:
        self.rooms = rooms
        self.district = district
        self.price = price

    def __repr__(self):
        return f"Repr a Home: rooms: {self.rooms}, district: {self.district}, price: {self.price:,}"

    def describe(self) -> str:
            return f"Describe a Home: rooms: {self.rooms}, district: {self.district}, price: {self.price:,}"


class Apartment(Home):
    def __init__(
        self,
        rooms: int,
        district: str,
        price: int,
        floor: int,
     ):
         super().__init__(rooms, district, price)
         self.floor = floor

    def describe(self) -> str:
                return f"Describe an Apartment: rooms: {self.rooms}, district: {self.district}, price: {self.price:,}, floor: {self.floor}"


class Tent(Home):
    pitched: bool = False
    _stove: str = "None"

    def __init__(
        self,
        rooms: int,
        price: int,
        camouflage: bool,
    ):
        super().__init__(rooms, None, price)
        self.camouflage = camouflage

    def __str__(self):
        return f"Str a Tent with {self.rooms} rooms, in district {self.district}, with price: {self.price:,}, {'it is pitched' if self.pitched else 'it is not pitched'}, and {'a great' if self.camouflage else 'no'} camouflage"

    def __repr__(self):
        return f"Repr a Tent: rooms: {self.rooms}, district: {self.district}, price: {self.price:,}, pitched: {self.pitched} camouflage: {self.camouflage}"

    def pitchTent(self, doPitch: bool):
        if not isinstance(doPitch, bool):
             raise ValueError("A tent being pitched is a bool, you fool!!!")
        self.pitched = doPitch

    @property
    def stove(self):
        return self._stove

    @stove.setter
    def stove(self, material):
         self._stove = material


#apt = Apartment(4, "Täby", 4_000_000, 3)
#print(apt)
#print(apt.describe())

tent = Tent(1, 5_000, True)
# Print with the str function.
print(tent) # Prints with str: str has precedence over repr if one exists.
print(f"{tent!s}")
print(tent.__str__())
# Print with the repr function.
print(f"{tent!r}")
print(tent.__repr__())

isAHome = isinstance(tent, Home)
print(f"A tent is a Home? {isAHome}")

print(f"Pitched? {tent.pitched}")
tent.pitchTent(True)
print(f"Pitched? {tent.pitched}")

print(f"Stove? {tent.stove}")
print(tent._stove)
print(tent.stove)
tent.stove = "Iron"
print(f"Stove? {tent.stove}")
tent._stove = "Stone"
print(f"Stove? {tent.stove}")

all_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = [n for n in all_numbers if n % 2 == 1]
even_numbers = [n for n in all_numbers if n % 2 == 0]
print(odd_numbers)
print(even_numbers)

