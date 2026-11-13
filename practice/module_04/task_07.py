from listings import Home, Listing, EstateAgent

kim = EstateAgent("Kim", "031-390 06 00")
home = Home("A01", "Majorna", 50, 2_453_000, "yes")
listing_1 = Listing(home, kim, 2_495_000)
listing_2 = Listing(home, kim, 2_495_000)

kim.phone = "031-390 06 01"

print(listing_1.agent.phone)
print(listing_2.agent.phone)