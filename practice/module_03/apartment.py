import csv
from pathlib import Path
import os

# Functions out here
def read_data_from_csv_file():
    pass

def clean_data_from_csv_file():
    pass


class Teve():
    # Constructor
    def __init__(self):
        self._is_on = False

    # Destructor
    def __del__(self):
        print("Destroy!")

    # Getter
    @property
    def is_on(self):
        return self._is_on

    # Setter
    @is_on.setter
    def is_on(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("Value must be a boolean!")
        self._is_on = value


# teve = Teve()
# print(teve.is_on)
# teve.is_on = True
# print(teve.is_on)


class Apartment():
    # Class variables
    default_price = 0
    default_sqm = 0

    @classmethod
    def get_defaults_class(cls):
        return f"{cls.default_price}, {cls.default_sqm}"
    @staticmethod
    def get_defaults_static():
        return f"{Apartment.default_price}, {Apartment.default_sqm}"

    def __init__(self, price, sqm):
        # Instance variables
        self.price = price
        self.sqm = sqm

    def __add__(self, other):
        return self.price + other.price

    # Method in here
    def get_sqm_price(self, total_sqm: int, total_price: int) -> int:
        return total_price // total_sqm


apt_1 = Apartment(1_000_000, 50)
apt_2 = Apartment(500_000, 30)
# print(apt_1.__add__(apt_2))

# apts = [Apartment]
# apts.append(apt_1)
# print(len(apts))
# for apt in apts:
#     print(apt)

# sqm_price = apartment_1.get_sqm_price(apt_sqm, apt_price)
# print(sqm_price)
# print(apartment.price, apartment.sqm)
# print(apartment.default_price, apartment.default_sqm)
# print(Apartment.default_price, Apartment.default_sqm)
# Apartment.get_defaults_class()
# Apartment.get_defaults_static()


class Parent1():
    name = "Sune"

class Parent2():
    age = 50

class Parent3():
    car = "Volvo"

class Parent4():
    computers = ["Mac", "PC"]

class Child1(Parent1, Parent2, Parent3, Parent4):
    pass

# child = Child1()
# print(type(Child1)) # <class 'type'>
# print(type(child)) # <class '__main__.Child1'>
# print(isinstance(Child1, type))  # True
# print(isinstance(child, Child1)) # True
# print(isinstance(child, type))   # False
# print(child.name, child.age, child.car, child.computers)