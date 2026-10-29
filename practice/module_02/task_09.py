from apartments import apartments

has_elevator = 0

for apt in apartments:
    if apt['elevator'] == 'yes':
        has_elevator += 1

print(has_elevator)