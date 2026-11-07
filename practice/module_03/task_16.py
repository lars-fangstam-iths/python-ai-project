from animals import Animal, Cow, Horse

animals = [
    Cow("Daisy"),
    Horse("Storm", 160),
    Horse("Thunder", 220),
    Animal("Kittypoo"),
]

horseCount = 0
horseIsAnimal = 0
for animal in animals:
    if isinstance(animal, Horse):
        horseCount += 1
        if (isinstance(animal, Animal)):
            horseIsAnimal += 1

print(horseCount)
print(f"Is a horse an animal? {'Yes' if horseIsAnimal else 'No'}!")
