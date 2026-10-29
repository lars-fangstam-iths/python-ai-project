from apartments import apartments

first = apartments[0]

print("f string")
for key, value in first.items():
    print(f"{key}: {type(value)}")

print("f string not necessary")
for key, value in first.items():
    print(key, type(value))