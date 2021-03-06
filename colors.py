import matplotlib.colors as mcolors
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict  # , Tuple

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


COLOR_SETS = [
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

LOW_V = [name for tup, name in [(t, x) for t, x in by_hsv] if tup[2] < 0.7]
HIGH_V = [name for tup, name in [(t, x) for t, x in by_hsv] if tup[2] >= 0.7]

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

        This function is useful when logging the colors used, 
        especially if color families are fetched randomly.

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


def get_random_color(n: int = 1, low: int = 0, high: int = 148) -> List:
    """ Get a completely random color

        If you specify a `low` and `high` you can pick the colors from a specific range of CSS4 Colors 

        Parameters
        ----------
        n : int
            number of colors desired. Default is 1. If n is 1, just the color_name is return, not a list

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
    colors = [mcolor_names[np.random.randint(low=low, high=high)] for _ in range(n)]
    if n == 1:
        return colors[0]
    else:
        return colors


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


def get_random_colorfamily():
    """ Will return one COLOR_Family """
    n = np.random.randint(len(COLOR_SETS))
    return COLOR_SETS[n]


def get_random_color_from_family(cfamily):
    """ Will return one colorname from the input list of colors 
    
    Parameters
    ==========
    cfamily: List
        List of names of colors
    """
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
            fam1 = get_random_colorfamily()
            if len(fam1) >= 6:
                done = 1
        fam_list.append(fam1)

    return fam_list


def display_color_strip(color_family, fc_bg="w"):
    """ A quick way to print a strip of colors given a list of colors 
    
    Parameters
    ==========

    color_family: List
        List of names of colors that Matplotlib recognizes. Typically, from `CSS4.colors <https://matplotlib.org/3.1.0/tutorials/colors/colors.html>`_

    fc_bg: color
        A single color to use as the background. Defaults to `'white'`

    """

    if isinstance(color_family, str):
        color_family = [color_family]

    num_rows = (len(color_family) - 1) // 8 + 1

    fig, ax = plt.subplots(figsize=(12, num_rows))
    fig.patch.set_facecolor(fc_bg)

    for row in range(num_rows):
        for x in range(8):
            try:
                r1 = patches.Rectangle(
                    (x * 12, 10 * row), 10, 7, color=color_family[8 * (row) + x]
                )
                ax.add_patch(r1)
            except:
                pass

    for row in range(num_rows, 0, -1):
        print(f"Row {row}: ", end="")
        for c in range(8):
            try:
                print(color_family[8 * (row - 1) + c], end=" ")
            except:
                pass
            if not (c + 1) % 8:
                print("\n")

    plt.axis("equal")
    name = _namestr(color_family)
    if name:
        plt.title(_namestr(color_family)[0])


def _namestr(obj, namespace=globals()):
    return [name for name in namespace if namespace[name] is obj]


ALLOWABLE_COLOR_ATTRS = ["random", "hue", "saturation", "sat", "value", "dark", "light"]
ALLOWABLE_COLOR_ORDERS = ["incr", "increasing", "decr", "decreasing"]

# hsv is of format ((h,s,v), "name")
sorted_hue = sorted(by_hsv, key=lambda x: x[0][0])
sorted_sat = sorted(by_hsv, key=lambda x: x[0][1])
sorted_value = sorted(by_hsv, key=lambda x: x[0][2])

hue_names = [name for _, name in sorted_hue]
sat_names = [name for _, name in sorted_sat]
value_names = [name for _, name in sorted_value]


def get_color_sequence(
    n: int = 6, attr: str = None, order: str = "incr", start_color=None, step: int = 1
) -> List:
    """ Returns a List of Color names, based on arguments specified

        If you specify a `low` and `high` you can pick the colors from a specific range of CSS4 Colors 


        Parameters
        ----------
        n : int, optional
            number of colors desired. Default is 6. If n is 1, just the color_name is return, not a list

        attr : str, optional
            Must be one of ['random', 'hue', 'sat|uration', 'value', 'dark', 'light'] or a color family name. 
            If 'random,' then order is ignored. Default `attr` is `hue`

        order : str, optional
            Must be either 'incr|easing' or 'decr|easing.' Default `order` is "increasing"
            

        Returns
        -------
        List
            List of n colors . Each element of the list is a color name. If n is 1, then just the name is returned, not a List. 

        Examples
        --------
        >>> get_color_sequence()
        ['red', 'mistyrose', 'salmon', 'tomato', 'darksalmon', 'coral']
        >>> get_color_sequence(1)
        'oldlace'
        >>> get_color_sequence(n=5, attr='Sat', order='incr')
        ['coral', 'orangered', 'lightsalmon', 'sienna', 'seashell']
        >>> get_color_sequence(n=3, attr='hue', order='incr', step=4)
        ['red', 'darksalmon', 'sienna']


    """
    # TODO Needed?
    if n > 100:
        raise Exception(f"{n} is too large. Should be less than 100.")

    if not attr:
        attr = "hue"
    if attr.lower() not in ALLOWABLE_COLOR_ATTRS:
        raise Exception(
            f"Unknown attr {attr}. Should be one of {ALLOWABLE_COLOR_ATTRS}"
        )

    if order.lower() not in ALLOWABLE_COLOR_ORDERS:
        raise Exception(
            f"Unknown attr {order}. Should be one of {ALLOWABLE_COLOR_ORDERS}"
        )

    if start_color is None:
        start_color = np.random.randint(len(sorted_sat) - n * step)

    if attr in ["sat" or "saturation"]:
        chosen_list = sat_names
    elif attr in ["val" or "value"]:
        chosen_list = value_names
    else:
        chosen_list = hue_names

    if order in ["incr", "increasing"]:
        _colors = chosen_list[start_color : start_color + (n * step) : step]
    else:
        _colors = chosen_list[start_color + (n * step) : start_color : -1 * step]

    if n == 1:
        return _colors[0]
    else:
        return _colors
