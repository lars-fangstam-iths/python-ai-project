from home import Home

apt1 = Home('A01', 'Majorna', 50, 2_453_000)
apt2 = Home('A06', 'Angered', 67, 1_481_000)

apts = [apt1, apt2]

for apt in apts:
    print(f"District: {apt.district}, Price: {apt.price}")