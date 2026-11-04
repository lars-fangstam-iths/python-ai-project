from home import Home

apt = Home('A01', 'Majorna', 100, 1_500_00)

print(apt.price)

apt.lower_price(100_000)

print(apt.price)

apt.lower_price(5_000_000)

print(apt.price)
