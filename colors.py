import matplotlib.colors as mcolors
import numpy as np


colors_d = mcolors.CSS4_COLORS
# Sort colors by hue, saturation, value and name
by_hsv = sorted(
    (tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(color))), name)
    for name, color in colors_d.items()
)
mcolor_names = [name for hsv, name in by_hsv]  # pluck the names, sorted by HSV

BLACK_WHITES = [
    "white",
    "whitesmoke",
    "gainsboro",
    "lightgrey",
    "silver",
    "darkgray",
    "gray",
    "dimgray",
    "black",
]

RED_BROWNS = [
    "maroon",
    "darkred",
    "brown",
    "firebrick",
    "indianred",
    "rosybrown",
    "lightsalmon",
    "darksalmon",
    "lightcoral",
    "salmon",
    "coral",
    "tomato",
    "orangered",
    "red",
]

GREENS = [
    "darkgreen",
    "green",
    "darkolivegreen",
    "olivedrab",
    "forestgreen",
    "seagreen",
    "mediumseagreen",
    "darkseagreen",
    "palegreen",
    "lightgreen",
    "greenyellow",
    "yellowgreen",
    "chartreuse",
    "lawngreen",
    "lime",
    "limegreen",
]


CYANS = mcolor_names[85:99]
BLUES = mcolor_names[100:121]
PURPLES = mcolor_names[122:132]
PINKS = mcolor_names[132:145]
GREYS = mcolor_names[1:11]

BEIGES = [
    "oldlace",
    "linen",
    "papayawhip",
    "blanchedalmond",
    "antiquewhite",
    "bisque",
    "moccasin",
    "wheat",
    "navajowhite",
    "burlywood",
    "tan",
]


YELLOWS = [
    "lightyellow",
    "cornsilk",
    "lemonchiffon",
    "lightgoldenrodyellow",
    "palegoldenrod",
    "yellow",
    "gold",
    "khaki",
    "goldenrod",
]

REDS = ["lightcoral", "salmon", "tomato", "orangered", "red", "crimson"]

BROWNS = ["peachpuff", "sandybrown", "peru", "chocolate", "sienna", "saddlebrown"]


ORANGES = [
    "lightsalmon",
    "darksalmon",
    "orange",
    "darkorange",
    "salmon",
    "coral",
    "tomato",
    "orangered",
]


color_sets = [
    REDS,
    ORANGES,
    PINKS,
    PURPLES,
    BLUES,
    CYANS,
    GREENS,
    YELLOWS,
    BEIGES,
    BROWNS,
    RED_BROWNS,
    BLACK_WHITES,
    GREYS,
]


LOW_SAT = [name for tup, name in [(t, x) for t, x in by_hsv] if tup[1] < 0.5]

HIGH_SAT = [name for tup, name in [(t, x) for t, x in by_hsv] if tup[1] > 0.5]


# Low SATURATION COLOR sets (PASTEL colors)
BLACK_WHITES_LOW_SAT = [
    name
    for tup, name in [(t, x) for t, x in by_hsv if x in BLACK_WHITES]
    if tup[1] < 0.6
]

BLUES_LOW_SAT = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in BLUES] if tup[1] < 0.7
]

BROWNS_LOW_SAT = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in BROWNS] if tup[1] < 0.8
]

CYAN_LOW_SAT = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in CYANS] if tup[1] < 0.6
]

GREENS_LOW_SAT = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in GREENS] if tup[1] < 0.7
]

PINKS_LOW_SAT = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in PINKS] if tup[1] < 0.7
]

PURPLES_LOW_SAT = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in PURPLES] if tup[1] < 0.7
]


RED_BROWNS_LOW_SAT = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in RED_BROWNS] if tup[1] < 0.7
]

YELLOWS_LOW_SAT = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in YELLOWS] if tup[1] < 0.8
]

# HIGH Value COLOR sets (STRONG colors)

BLUES_HIGH_SAT = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in BLUES] if tup[1] >= 0.7
]

BROWNS_HIGH_SAT = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in BROWNS] if tup[1] >= 0.8
]

CYAN_HIGH_SAT = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in CYANS] if tup[1] >= 0.6
]

GREENS_HIGH_SAT = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in GREENS] if tup[1] >= 0.7
]

PINKS_HIGH_SAT = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in PINKS] if tup[1] >= 0.7
]

PURPLES_HIGH_SAT = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in PURPLES] if tup[1] >= 0.7
]


RED_BROWNS_HIGH_SAT = [
    name
    for tup, name in [(t, x) for t, x in by_hsv if x in RED_BROWNS]
    if tup[1] >= 0.7
]

YELLOWS_HIGH_SAT = [mcolor_names[x] for x in [53, 63]]

# VALUES
# Low Value COLOR sets (darker colors)
BLACK_WHITES_LOW_V = [
    name
    for tup, name in [(t, x) for t, x in by_hsv if x in BLACK_WHITES]
    if tup[2] < 0.6
]

BLUES_LOW_V = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in BLUES] if tup[2] < 0.7
]

BROWNS_LOW_V = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in BROWNS] if tup[2] < 0.8
]

CYAN_LOW_V = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in CYANS] if tup[2] < 0.6
]

GREENS_LOW_V = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in GREENS] if tup[2] < 0.7
]

PINKS_LOW_V = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in PINKS] if tup[2] < 0.7
]

PURPLES_LOW_V = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in PURPLES] if tup[2] < 0.7
]


RED_BROWNS_LOW_V = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in RED_BROWNS] if tup[2] < 0.7
]

YELLOWS_LOW_V = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in YELLOWS] if tup[2] < 0.8
]

# HIGH Value COLOR sets (Lighter colors)
BLACK_WHITES_HIGH_V = [
    name
    for tup, name in [(t, x) for t, x in by_hsv if x in BLACK_WHITES]
    if tup[2] >= 0.6
]

BLUES_HIGH_V = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in BLUES] if tup[2] >= 0.7
]

BROWNS_HIGH_V = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in BROWNS] if tup[2] >= 0.8
]

CYAN_HIGH_V = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in CYANS] if tup[2] >= 0.6
]

GREENS_HIGH_V = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in GREENS] if tup[2] >= 0.7
]

PINKS_HIGH_V = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in PINKS] if tup[2] >= 0.7
]

PURPLES_HIGH_V = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in PURPLES] if tup[2] >= 0.7
]


RED_BROWNS_HIGH_V = [
    name
    for tup, name in [(t, x) for t, x in by_hsv if x in RED_BROWNS]
    if tup[2] >= 0.7
]

YELLOWS_HIGH_V = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in YELLOWS] if tup[2] >= 0.8
]

## Color Based Functions


def get_next_color(
    color_list,
    col_index,
    p_next=0.1,
    use_color_families=False,
    curr_fam_index=0,
    p_next_fam=0,
):

    if use_color_families:
        # We have more than one color_family
        if np.random.random() < p_next_fam:
            curr_fam_index += 1
            col_index = 0
        chosen_fam = color_list[curr_fam_index % len(color_list)]
    else:
        chosen_fam = color_list  # all colors are in one family

    if np.random.random() < p_next:
        col_index += 1

    chosen_color = chosen_fam[col_index % len(chosen_fam)]

    return (chosen_color, curr_fam_index, col_index)


def get_rnd_color_family():
    n = np.random.randint(len(color_sets))
    return color_sets[n]
