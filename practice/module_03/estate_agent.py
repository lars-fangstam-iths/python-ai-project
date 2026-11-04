class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Cat(Animal):
    def speak(self):
        return "Meow"


class Dog(Animal):
    def __init__(self, name, tricks):
        super().__init__(name)
        self.tricks = tricks

    def speak(self):
        return "Woof"

class Horse(Animal):
    pass

luna = Cat("Luna")
rex = Dog("Rex", ["sit", "shake"])
brunte = Horse("Brunte")

for animal in [luna, rex, brunte]:
    print(animal.name, "says", animal.speak())

print(rex.tricks)
print(isinstance(rex, Animal))