import pytest
from listings import Home, ListingClass, EstateAgent

kim = EstateAgent("Kim", "031-390 06 00")
home = Home("A01", "Majorna", 50, 2_500_000, "yes")
listing = ListingClass(home, kim, 2_500_000)

# Run with: python3 -m pytest practice/module_04/test_listings.py

def test_price_per_sqm():
    assert(listing.price_per_sqm == 50_000)

def test_describe():
    assert(listing.describe() == "A01 in Majorna, 2,500,000 SEK, call Kim on 031-390 06 00.")

def test_refuse_invalid_price():
    with pytest.raises(ValueError):
        listing.asking_price = -1