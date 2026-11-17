# Run with: python3 -m pytest practice/module_04/test_vat.py

def add_vat(price):
    return round(price * 1.25)


def test_add_vat():
    assert add_vat(100) == 125