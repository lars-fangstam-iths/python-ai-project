import pandas as pd

pd.options.display.float_format = "{:,.0f}".format

sales = pd.DataFrame({
    "district": ["Majorna", "Angered", "Majorna", "Angered", "Centrum"],
    "price": [3_350_000, 1_880_000, 2_190_000, 1_490_000, 5_720_000],
    "living_area": [68, 74, 45, 61, 88],
})
sales["price"] = sales["price"].astype(float)

sales["price_per_sqm"] = sales["price"] / sales["living_area"]
by_price = sales.sort_values("price_per_sqm", ascending=False)
medians = sales.groupby("district")["price"].median()

print(f"Sorted by price per square meter:\n{by_price}")
print(f"\nMedian price per district:\n{medians}")