from apartments import apartments

def within_budget(apts, max_price):
    selected = []
    
    for apartment in apts:
        #print(type(apartment['price']), apartment['price'])

        if apartment['price'] < max_price:
            selected.append(apartment)

    return selected

cheap = within_budget(apartments, 2_000_000)
print(cheap)
print(len(cheap))

assert len(cheap) == 4

no_free_apts = within_budget(apartments, 0)
assert no_free_apts == []
assert len(no_free_apts) == 0