
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

def save_file(fig, title=None, details=None):
    SAVE_FILE = True
    if SAVE_FILE:
        fn = ''
        if title is not None:
            fn += title
            
        if details is not None:
            fn+= details
            
        dtstr = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%p")            

        #https://stackoverflow.com/questions/4804005/matplotlib-figure-facecolor-background-color
        #if you want the background color saved... you must get_facecolor()
        plt.savefig(f'../images/temp/{fn+dtstr}.jpg', facecolor=fig.get_facecolor(), edgecolor='none')

#https://stackoverflow.com/questions/30008322/draw-a-curve-connecting-two-points-instead-of-a-straight-line
def curved_line(point1, point2, resolution=100):

    a = (point2[1] - point1[1])/(np.cosh(point2[0]) - np.cosh(point1[0]))
    b = point1[1] - a*np.cosh(point1[0])
    x = np.linspace(point1[0], point2[0], resolution)
    y = a*np.cosh(x) + b

    return (x,y)


#Needed for the Bezier Curve function below
def recta(x1, y1, x2, y2):
    a = (y1 - y2) / (x1 - x2)
    b = y1 - a * x1
    return (a, b)


def bezier_curve(start_pt, end_pt, mid_pt, resolution=1000):

    xa, xb, xc = start_pt[0], mid_pt[0], end_pt[0]
    (x1, y1, x2, y2) = (start_pt[0], start_pt[1], mid_pt[0], mid_pt[1])
    (a1, b1) = recta(start_pt[0], start_pt[1], mid_pt[0], mid_pt[1])
    (a2, b2) = recta(mid_pt[0], mid_pt[1], end_pt[0], end_pt[1])

    bez_pts = []
    for i in range(0, resolution):
        if x1 == x2:
            continue
        else:
            (a, b) = recta(x1, y1, x2, y2)
        x = x1 + i*(x2 - x1)/resolution
        y = a*x + b
        bez_pts.append((x,y))
        x1 += (xb - xa)/resolution
        y1 = a1*x1 + b1
        x2 += (xc - xb)/resolution
        y2 = a2*x2 + b2

    return bez_pts
