location = (57.70, 11.97)

changed = (57.71, location[1])
print(changed)
location = changed
print(location)

location[0] = 57.71
# TypeError: 'tuple' object does not support item assignment
# Values in a Tuple can not change
