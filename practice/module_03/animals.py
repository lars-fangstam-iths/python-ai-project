class Animal():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{type(self).__name__}:({self.name!r})"

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} says {self.speak()}"

class Cow(Animal):
    def speak(self):
        return "Moo"

class Horse(Animal):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    def speak(self):
        return "Neigh"

    def describe(self):
        return f"{super().describe()}, and is {self.height} cm tall"