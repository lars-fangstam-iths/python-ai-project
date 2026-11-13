from listings import Home, Listing, EstateAgent

kim = EstateAgent("Kim", "031-390 06 00")
home = Home("A01", "Majorna", 50, 2_453_000, "yes")
listing = Listing(home, kim, 2_495_000)

print(listing.describe())