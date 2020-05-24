
import logging
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt


def draw_line(xy1, xy2, ax, **kwargs):
    """ Connect pt1 (x1,y1) to pt2 (x2, y2) """    
    x_arr = [xy1[0], xy2[0]]
    y_arr = [xy1[1], xy2[1]]
    edge = Line2D([x_arr],[y_arr], **kwargs)
    ax.add_line(edge)

    return ax,



def plot_label(xy, text):
    y = xy[1] - 0.15  # shift y-value for label so that it's below the artist
    plt.text(xy[0], y, text, ha="center", family='sans-serif', size=10)


def save_file(fig, title=None, nbk=None, num_rows=None, num_cols=None, details=None, SAVE_FILE = True):

    if SAVE_FILE:
        fn = ''
        if nbk is not None:
            fn+= str(nbk)
        if num_rows is not None:
            fn+= str(num_rows)
        if num_cols is not None:
            fn+= str(num_cols)
        if title is not None:
            fn += title
            
        if details is not None:
            fn+= details
            
        dtstr = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%p")            

        #https://stackoverflow.com/questions/4804005/matplotlib-figure-facecolor-background-color
        #if you want the background color saved... you must get_facecolor()
        plt.savefig(f'../images/temp/{fn+dtstr}.jpg', facecolor=fig.get_facecolor(), edgecolor='none')

        logging.info(f'Saved to ../images/temp/{fn+dtstr}.jpg')


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
