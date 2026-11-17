from listings import Home, EstateAgent, ListingClass as Listing, SavedSearch

listing1 = Listing(Home("A01", "Majorna", 50, 10_000_000), EstateAgent("Kim", "031-390 06 00"), 3_000_000)
listing2 = Listing(Home("A02", "Majorna", 50, 1_000_000), EstateAgent("Kim", "031-390 06 00"), 4_000_000)
listing3 = Listing(Home("A03", "Angered", 50, 2_000_000), EstateAgent("Kim", "031-390 06 00"), 2_000_000)

savedSearch = SavedSearch("Majorna", 3_000_000)

if savedSearch.matches(listing1):
    print(listing1.describe())

if savedSearch.matches(listing2):
    print(listing2.describe())

if savedSearch.matches(listing3):
    print(listing3.describe())
