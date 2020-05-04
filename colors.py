import matplotlib.colors as mcolors

colors_d = mcolors.CSS4_COLORS
# Sort colors by hue, saturation, value and name
by_hsv = sorted(
    (tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(color))), name)
    for name, color in colors_d.items()
)
mcolor_names = [name for hsv, name in by_hsv]  # pluck the names, sorted by HSV


BLACK_WHITES = mcolor_names[:13]
RED_BROWNS = mcolor_names[14:29]
BROWNS = mcolor_names[29:36]
BEIGES = mcolor_names[36:49]
YELLOWS = mcolor_names[50:64]
GREENS = mcolor_names[64:81]
CYANS = mcolor_names[85:99]
BLUES = mcolor_names[100:121]
PURPLES = mcolor_names[122:132]
PINKS = mcolor_names[132:145]

red_indices = [21, 22, 23, 24, 25, 26, 27, 145]
REDS = [mcolor_names[x] for x in red_indices]


color_sets = [
    REDS,
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
BLACK_WHITES_HIGH_SAT = [
    name
    for tup, name in [(t, x) for t, x in by_hsv if x in BLACK_WHITES]
    if tup[1] >= 0.6
]

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

YELLOWS_HIGH_SAT = [
    name for tup, name in [(t, x) for t, x in by_hsv if x in YELLOWS] if tup[1] >= 0.8
]

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
