class Animal():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{type(self).__name__}: {self.name!r}"

    def speak(self):
        return "..."

class Cow(Animal):
    def speak(self):
        return "Moo"