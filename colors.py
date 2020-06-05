import matplotlib.colors as mcolors
import numpy as np
from typing import List, Dict, Tuple


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

CYANS = [
    "teal",
    "darkcyan",
    "lightseagreen",
    "darkturquoise",
    "mediumturquoise",
    "paleturquoise",
    "turquoise",
    "aquamarine",
    "aqua",
    "cyan",
]

BLUES = [
    "midnightblue",
    "navy",
    "darkblue",
    "mediumblue",
    "royalblue",
    "steelblue",
    "lightsteelblue",
    "lightblue",
    "lavender",
    "powderblue",
    "skyblue",
    "lightskyblue",
    "deepskyblue",
    "cornflowerblue",
    "dodgerblue",
]


PINKS = [
    "purple",
    "darkmagenta",
    "mediumvioletred",
    "orchid",
    "plum",
    "violet",
    "hotpink",
    "deeppink",
    "fuchsia",
    "magenta",
]

PURPLES = [
    "indigo",
    "rebeccapurple",
    "darkslateblue",
    "slateblue",
    "mediumpurple",
    "mediumslateblue",
    "mediumorchid",
    "blueviolet",
    "darkorchid",
    "darkviolet",
]


GREYS = [
    "dimgray",
    "dimgrey",
    "gray",
    "grey",
    "darkgray",
    "darkgrey",
    "silver",
    "lightgray",
    "lightgrey",
    "gainsboro",
]

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


color_family_dict = {
    "Beiges": BEIGES,
    "black_whites": BLACK_WHITES,
    "Blues": BLUES,
    "browns": BROWNS,
    "Cyans": CYANS,
    "Greens": GREENS,
    "Greys": GREYS,
    "Oranges": ORANGES,
    "Pinks": PINKS,
    "Purples": PURPLES,
    "red_browns": RED_BROWNS,
    "Reds": REDS,
    "Yellows": YELLOWS,
}


def get_key_given_item(v, _dict: Dict):
    """
    Get list of keys from a dictionary, given its value. Reverse lookup
    """

    keys = [key for (key, value) in _dict.items() if value == v]
    return keys


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


def print_color_family_names(cfams):
    """ Print the Color Family Name instead of printing out each element 

        This function is useful in logging the colors used, especially if random color families are fetched.

        Parameters
        ----------

        cfams: List
            One or more Color Families, pre-specified. Each element is a list of colornames
            
    """
    return_str = ""
    for f in cfams:
        if f in color_family_dict.values():
            keys = get_key_given_item(f, color_family_dict)
            return_str += [str(k) for k in keys]
        else:
            return_str += str(f)

    return return_str


def get_random_color(n: int, low: int = 0, high: int = 148) -> List:
    """ Get a completely random color

        If you specify a `low` and `high` you can pick the colors from a specific range of CSS4 Colors 

        Parameters
        ----------
        n : int
            number of colors desired

        low : int
            lower end to pick range of mcolornames (Default is 0)

        high : int
            upper end to pick range of mcolornames (Default is 148)

        Returns
        -------
        List
            List of n colors . Each element is a color name 
        
    """

    # TODO: Need to handle replacement=True/False later
    return [mcolor_names[np.random.randint(low=low, high=high)] for _ in range(n)]


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


def get_rnd_family():
    n = np.random.randint(len(color_sets))
    return color_sets[n]


def get_rnd_color_from_family(cfamily):
    n = np.random.randint(len(cfamily))
    return cfamily[n]


def get_n_random_color_families(n: int = 2) -> List:
    """ Returns a specified number n of randomly selected color families

        Parameters
        ----------

        n : int
            number of color families desired
        
        Returns
        -------
        List
            List of n color families. each Element (COLOR FAMILY) is a list of color names 
        

    """

    fam_list = []
    for _ in range(n):
        done = 0
        while not done:
            fam1 = get_rnd_family()
            if len(fam1) >= 6:
                done = 1
        fam_list.append(fam1)

    return fam_list


def _display_color_strip(color_family, fc_bg="w"):
    """ A quick way to print a strip of colors given a list of colors """

    size = 1
    num_rows = (len(color_family) - 1) // 10 + 1
    hg = HexGrid(num_rows, 10, size, flat=False)

    fig, ax = plt.subplots(figsize=(12, num_rows))
    fig.patch.set_facecolor(fc_bg)

    for idx, h in enumerate(hg.hlist):
        try:
            fc = color_family[idx]
            border = "black"
            h.render(fc=fc, color=border, lw=2)
            # lab = str(idx) +'\n' + ', '.join([str(c) for c in (h.xc,h.yc,h.zc)])
            # plot_label((h.x,h.y), lab)
        except:
            pass

    for row in range(num_rows, 0, -1):
        print(f"Row {row}: ", end="")
        for c in range(10):
            try:
                print(color_family[10 * (row - 1) + c], end=" ")
            except:
                pass
            if not (c + 1) % 10:
                print("\n")

    plt.axis("equal")
    plt.title(namestr(color_family)[0])
