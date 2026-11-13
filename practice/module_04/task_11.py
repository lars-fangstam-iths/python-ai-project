from listings import Home, ListingClass, EstateAgent

kim = EstateAgent("Kim", "031-390 06 00")
home = Home("A01", "Majorna", 50, 2_453_000, "yes")
listing = ListingClass(home, kim, 2_495_000)

listing.asking_price = -1

print(listing.describe())