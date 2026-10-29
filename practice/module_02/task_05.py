from apartments import apartments

districts = {apartment['district'] for apartment in apartments}
sorted = sorted(districts)

print("Unsorted ", districts)
print("Sorted ", sorted)