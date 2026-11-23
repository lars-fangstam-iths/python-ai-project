import sys
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
# print("BASE_DIR",BASE_DIR) # python-ai-project

sys.path.insert(0, str(BASE_DIR))
from practice.data.mushroom_mappings import columns, mappings

path = Path('practice') / 'data' / 'mushrooms.csv'
df = pd.read_csv(path, header=None, names=columns)

df = df.replace(mappings)

print(df.shape)
print(df.info())
print(df.head())
print(df["class"].value_counts())

# Value	Column	Meaning
# p	class	Poisonous
# x	cap_shape	Convex
# s	cap_surface	Smooth
# n	cap_color	Brown
# t	bruises	Bruises
# p	odor	Pungent
# f	gill_attachment	Free
# c	gill_spacing	Close
# n	gill_size	Narrow
# k	gill_color	Black
# e	stalk_shape	Enlarging
# e	stalk_root	Equal
# s	stalk_surface_above_ring	Smooth
# s	stalk_surface_below_ring	Smooth
# w	stalk_color_above_ring	White
# w	stalk_color_below_ring	White
# p	veil_type	Partial
# w	veil_color	White
# o	ring_number	One
# p	ring_type	Pendant
# k	spore_print_color	Black
# s	population	Scattered
# u	habitat	Urban