# Used AI to help with importing the mushroom dataset and to create these mappings.

columns = [
    "class",
    "cap_shape",
    "cap_surface",
    "cap_color",
    "bruises",
    "odor",
    "gill_attachment",
    "gill_spacing",
    "gill_size",
    "gill_color",
    "stalk_shape",
    "stalk_root",
    "stalk_surface_above_ring",
    "stalk_surface_below_ring",
    "stalk_color_above_ring",
    "stalk_color_below_ring",
    "veil_type",
    "veil_color",
    "ring_number",
    "ring_type",
    "spore_print_color",
    "population",
    "habitat"
]

mappings = {
    "class": {
        "e": "edible",
        "p": "poisonous"
    },
    "cap_shape": {
        "b": "bell",
        "c": "conical",
        "x": "convex",
        "f": "flat",
        "k": "knobbed",
        "s": "sunken"
    },
    "cap_surface": {
        "f": "fibrous",
        "g": "grooves",
        "y": "scaly",
        "s": "smooth"
    },
    "cap_color": {
        "n": "brown",
        "b": "buff",
        "c": "cinnamon",
        "g": "gray",
        "r": "green",
        "p": "pink",
        "u": "purple",
        "e": "red",
        "w": "white",
        "y": "yellow"
    },
    "bruises": {
        "t": "yes",
        "f": "no"
    },
    "odor": {
        "a": "almond",
        "l": "anise",
        "c": "creosote",
        "y": "fishy",
        "f": "foul",
        "m": "musty",
        "n": "none",
        "p": "pungent",
        "s": "spicy"
    },
    "gill_attachment": {
        "a": "attached",
        "d": "descending",
        "f": "free",
        "n": "notched"
    },
    "gill_spacing": {
        "c": "close",
        "w": "crowded",
        "d": "distant"
    },
    "gill_size": {
        "b": "broad",
        "n": "narrow"
    },
    "gill_color": {
        "k": "black",
        "n": "brown",
        "b": "buff",
        "h": "chocolate",
        "g": "gray",
        "r": "green",
        "o": "orange",
        "p": "pink",
        "u": "purple",
        "e": "red",
        "w": "white",
        "y": "yellow"
    },
    "stalk_shape": {
        "e": "enlarging",
        "t": "tapering"
    },
    "stalk_root": {
        "b": "bulbous",
        "c": "club",
        "u": "cup",
        "e": "equal",
        "z": "rhizomorphs",
        "r": "rooted",
        "?": "unknown"
    },
    "stalk_surface_above_ring": {
        "f": "fibrous",
        "y": "scaly",
        "k": "silky",
        "s": "smooth"
    },
    "stalk_surface_below_ring": {
        "f": "fibrous",
        "y": "scaly",
        "k": "silky",
        "s": "smooth"
    },
    "stalk_color_above_ring": {
        "n": "brown",
        "b": "buff",
        "c": "cinnamon",
        "g": "gray",
        "o": "orange",
        "p": "pink",
        "e": "red",
        "w": "white",
        "y": "yellow"
    },
    "stalk_color_below_ring": {
        "n": "brown",
        "b": "buff",
        "c": "cinnamon",
        "g": "gray",
        "o": "orange",
        "p": "pink",
        "e": "red",
        "w": "white",
        "y": "yellow"
    },
    "veil_type": {
        "p": "partial",
        "u": "universal"
    },
    "veil_color": {
        "n": "brown",
        "o": "orange",
        "w": "white",
        "y": "yellow"
    },
    "ring_number": {
        "n": "none",
        "o": "one",
        "t": "two"
    },
    "ring_type": {
        "c": "cobwebby",
        "e": "evanescent",
        "f": "flaring",
        "l": "large",
        "n": "none",
        "p": "pendant",
        "s": "sheathing",
        "z": "zone"
    },
    "spore_print_color": {
        "k": "black",
        "n": "brown",
        "b": "buff",
        "h": "chocolate",
        "r": "green",
        "o": "orange",
        "u": "purple",
        "w": "white",
        "y": "yellow"
    },
    "population": {
        "a": "abundant",
        "c": "clustered",
        "n": "numerous",
        "s": "scattered",
        "v": "several",
        "y": "solitary"
    },
    "habitat": {
        "g": "grasses",
        "l": "leaves",
        "m": "meadows",
        "p": "paths",
        "u": "urban",
        "w": "waste",
        "d": "woods"
    }
}