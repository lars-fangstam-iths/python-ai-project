def add_vat(price):
    return round(price * 1.25)


def test_add_vat():
    assert add_vat(100) == 125