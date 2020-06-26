from datetime import datetime
import math
from math import pi, sin, cos, sqrt

from matplotlib.lines import Line2D
import matplotlib.patches as mpatches
from matplotlib.patches import Arc, Circle, Ellipse, Polygon, Wedge
import matplotlib.pyplot as plt
import numpy as np
from typing import List


PI = math.pi

# DEFINE POLYGONS INSIDE A HEXAGON
# Rhombuses are made up of 3 Adjacent vertices and the Center
PENTA0, PENTA1, PENTA2 = (0, 1, 2, 3, 4), (1, 2, 3, 4, 5), (2, 3, 4, 5, 0)
PENTA3, PENTA4, PENTA5 = (3, 4, 5, 0, 1), (4, 5, 0, 1, 2), (5, 0, 1, 2, 3)
HHEX0, HHEX1, HHEX2 = (0, 1, 2, 3), (1, 2, 3, 4), (2, 3, 4, 5)
HHEX3, HHEX4, HHEX5 = (3, 4, 5, 0), (4, 5, 0, 1), (5, 0, 1, 2)

RHOMBUS0, RHOMBUS1, RHOMBUS2 = (0, 1, 2), (1, 2, 3), (2, 3, 4)
RHOMBUS3, RHOMBUS4, RHOMBUS5 = (3, 4, 5), (4, 5, 0), (5, 0, 1)
VTRIANGLE0, VTRIANGLE1, VTRIANGLE2 = (0, 1, 2), (1, 2, 3), (2, 3, 4)
VTRIANGLE3, VTRIANGLE4, VTRIANGLE5 = (3, 4, 5), (4, 5, 0), (5, 0, 1)
TRIANGLES = ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0))
CTRIANGLE0, CTRIANGLE1, CTRIANGLE2 = (0, 1), (1, 2), (2, 3)
CTRIANGLE3, CTRIANGLE4, CTRIANGLE5 = (3, 4), (4, 5), (5, 0)
CTRIANGLES = [CTRIANGLE0, CTRIANGLE1, CTRIANGLE2, CTRIANGLE3, CTRIANGLE4, CTRIANGLE5]
ALLOWABLE_POLYGONS = [
    RHOMBUS0,
    RHOMBUS1,
    RHOMBUS2,
    RHOMBUS3,
    RHOMBUS4,
    RHOMBUS5,
    CTRIANGLE0,
    CTRIANGLE1,
    CTRIANGLE2,
    CTRIANGLE3,
    CTRIANGLE4,
    CTRIANGLE5,
    HHEX0,
    HHEX1,
    HHEX2,
    HHEX3,
    HHEX4,
    HHEX5,
    PENTA0,
    PENTA1,
    PENTA2,
    PENTA3,
    PENTA4,
    PENTA5,
]

RHOMBUSES1 = {"west": (0, 1, 2), "northeast": (2, 3, 4), "southwest": (4, 5, 0)}
RHOMBUSES2 = {"northwest": (1, 2, 3), "east": (3, 4, 5), "south": (5, 0, 1)}
SPOKES_3A = (1, 3, 5)
SPOKES_3B = (0, 2, 4)

VERT_NUM = ["v0", "v1", "v2", "v3", "v4", "v5"]
VERT_NAMES = ["vertices", "vertex"] + VERT_NUM
EDGE_NUM = ["e0", "e1", "e2", "e3", "e4", "e5"]
EDGE_NAMES = ["edge", "edges"] + EDGE_NUM


def hex_corner(center, size, i, flat=True):
    """Return the ith vertex of a regular hex with center of size i and flat/pointy orientation"""

    if flat:
        angle_rad = PI / 180 * (60 * i)
    else:
        angle_rad = PI / 180 * (60 * i - 30)

    # return Point(center.x + size * cos(angle_rad),
    #              center.y + size * sin(angle_rad))
    return (center[0] + size * cos(angle_rad), center[1] + size * sin(angle_rad))


def get_pt_rtheta_away(pt, dist, theta):
    """ Given a point (x,y) and a certain dist at an angle theta, returns the point (x,y)"""
    x = pt[0] + dist * sin(theta * PI / 180)  # x
    y = pt[1] + dist * cos(theta * PI / 180)  # y
    return (x, y)


SPOKE_MIRROR_X = [0, 5, 4, 3, 2, 1]
SPOKE_MIRROR_Y = [4, 3, 2, 1, 0, 5]
SPOKE_MIRROR_Z = [2, 1, 0, 5, 4, 3]
APO_MIRROR_X = [5, 4, 3, 2, 1, 0]
APO_MIRROR_Y = [3, 2, 1, 0, 5, 4]
APO_MIRROR_Z = [1, 0, 5, 4, 3, 2]


class Hex:
    """Represents one Hexagon. Typically on a hexagonal grid
    
    The hexagon can be flat topped (flat = True) or pointy-topped (flat=False)
    Each Hexagon has:
    a center (x,y)
    size (of its edge)
    flat = True (or False if Pointy-topped)
    verts = xy of its 6 vertices
    h = height of the hexaxon from top to bottom
    w = width = distance between 2 adjacent centers to the right/left of each other
    
    """

    def __init__(self, x=0, y=0, size=1, id=None, flat=True, w=None, cube=None):
        """Define properties of one single Hexagon"""
        self.x = x
        self.y = y
        self.center = (x, y)
        self.id = id
        self.size = size
        self.flat = flat
        self.verts = None
        self.lattice = None  # will be computed only when get_lattice_points is invoked

        # Cube coordinates
        self.xc, self.yc, self.zc = (None, None, None)

        if self.flat:
            self.ht = sqrt(3) * size
            self.w = 2 * size
        else:
            self.w = sqrt(3) * size
            self.ht = 2 * size

        self.cube = cube  # cube coords of this particular hex
        self.row = None
        self.column = None

    def __str__(self):
        desc = "Flat" if self.flat else "Pointy"
        return f" {desc}-Hex @ {(self.x,self.y)} size {self.size}"

    def get_verts(self):
        """ Calculate all 6 verticles of the hex"""
        verts = []
        for v in range(6):
            verts.append(hex_corner(self.center, self.size, v, self.flat))

        self.verts = verts
        return self.verts

    def get_lattice_points(self, density=2):
        """
            This method serves two purposes. It will store the interior 'lattice' points of a hexagon in a 
            dictionary called `lattice` which can then be used. It also returns the 
            dictionary, for plotting purposes.

        Parameters
        ----------
        
        density, optional
            Currently only 2 has been implemented.

        Returns
        -------
        Dictionary
            A dictionary of lattice points, with keys = ['ab', 'ea', 'eb','sa', 'sb',]

        """

        lat = {}
        lat["c"] = self.center
        lat["v"] = self.get_verts()  # 6

        # TODO if density == 1

        if density == 2:
            etp = self.point(pt_name="edge", action="trisect")  # 12 points
            stp = self.point(pt_name="spoke", action="trisect")  # 12 points
            # for flat hexagons only...caution
            atp = self.point(
                pt_name="apo", dist=2 / 3 * self.ht / 2 / self.size
            )  # 6 points

            # adding a 7th point to avoid ugly (v+1)%6 type operations
            # add the entire list again?
            lat["ea"] = etp[:6] + [etp[0]]
            lat["eb"] = etp[6:] + [etp[6]]
            lat["sa"] = stp[:6] + [stp[0]]
            lat["sb"] = stp[6:] + [stp[6]]
            lat["ab"] = atp + [atp[0]]  # the second point b along the aptothem

        self.lattice = lat
        return lat

    def get_symmetrical_point(self, lattice_tup, axis="6"):
        """ 
        Given a lattice point inside a hexagon, returns symmetrical point(s) per axis specified.

        Given one point on the lattice, this method will return all 6 of its 
        reflected siblings, or, if an `axi` is specified, will return that 
        particular mirror reflected point. Note that this is MIRROR reflection, 
        not rotational symmetry. Use axi = '6' for rotational symmetry.

        Parameters
        ----------

        lattice_tup: tuple
            This tuple is made up of a `pt_name` and an `index` specifying the lattice point uniquely.
            pt_name: string. A special name to denote specific lattice points. Allowable values are:
            ['sa', 'sb', 'ea', 'eb', 'ab']
            
            index: integer  index specifies which spoke or apothem to use for theta offset. Valid values are 
            integers from 0..5

        axis: string, optional
            The Axis of reflective symmetry. Should be one of 'x', 'y', 'z', or '6'.

        Returns
        -------
        Tuple
            an (x, y) tuple of the symmetrical point, or 6 points in [(x1,y1), (x2,y2) ...] format

        Examples
        --------
        >>> h = Hex(0, 0, size=1)
        >>> h.get_lattice_points()
        >>> symp = h.get_symmetrical_points(("ab", 4), "z")

        """

        axis = axis.lower()
        if axis not in ["x", "y", "z", "6"]:
            raise ValueError(f"faulty axis specified for reflection")

        pt_name, pindex = lattice_tup  # name and index

        if self.lattice is None:
            self.get_lattice_points()

        if axis == "6" or None:
            return self.lattice[pt_name]
        if axis == "x":
            if pt_name in ["sa", "sb"]:
                mirror = SPOKE_MIRROR_X
            elif pt_name in ["aa", "ab", "ea", "eb"]:
                mirror = APO_MIRROR_X
        elif axis == "y":
            if pt_name in ["sa", "sb"]:
                mirror = SPOKE_MIRROR_Y
            elif pt_name in ["aa", "ab", "ea", "eb"]:
                mirror = APO_MIRROR_Y
        elif axis == "z":
            if pt_name in ["sa", "sb"]:
                mirror = SPOKE_MIRROR_Z
            elif pt_name in ["aa", "ab", "ea", "eb"]:
                mirror = APO_MIRROR_Z

        # For points on the edge, distance from vertex comes into play.
        # Adjusting for that...
        if pt_name == "ea":
            ref_name = "eb"
        elif pt_name == "eb":
            ref_name = "ea"
        else:
            ref_name = pt_name

        return self.lattice[ref_name][mirror[pindex]]

    def get_points_on_edge(self, edge=None, dist_frac=None):
        """
        Given a Edgenum [0-5] return a point(x,y) distance from vert away on the edge     

        Parameters
        ----------

        edge: int or None
            edge is the edge-number from 0..5. If it is None, all 6 edges are included.

        dist_frac : float
            distance from the hexagon vertex, in hexagon-size units. Note: This is not absolute distance. Typically
            `dist` goes from 0 to 1, and gets multiplied by the `size` of the hexagon. 
            0 is closest to the starting vertex, 1 is the next vertex.

        Returns
        -------
        list
            List of new points, in [(x1,y1), (x2,y2) ...] format


        """

        if self.flat:
            theta_offset = 30
        else:
            theta_offset = -60

        if dist_frac is None:  # then a random distance (0, size) is generated
            dist = np.random.random() * self.size
        else:
            dist = dist_frac * self.size

        new_pts = []
        if edge not in range(6):
            pts = self.verts
            for v, pt in enumerate(pts):  # 1 or all 6
                new_pts.append(
                    (
                        pt[0]
                        + dist * sin((-60 * (v + 1) + theta_offset) * PI / 180),  # x
                        pt[1] + dist * cos((-60 * (v + 1) + theta_offset) * PI / 180),
                    )  # y
                )
        else:  # one specific edge
            pt = self.verts[edge]
            new_pts.append(
                (
                    pt[0] + dist * sin((-60 * (edge + 1) + theta_offset) * PI / 180),
                    pt[1] + dist * cos((-60 * (edge + 1) + theta_offset) * PI / 180),
                )  # y
            )

        return new_pts

    def get_points_dist_from_vertex(self, dist, theta):
        """ Return 6 points that are dist and angle theta away from each of the 6 vertices 
        
        Note that these points may or may not be on an edge.
        To be on the edge, theta gets fixed

        Parameters
        ----------

        dist : float
            distance from the hexagon vertex, in hexagon-size units. Note: This is not absolute distance. Typically
            `dist` goes from 0 to 1, and gets multiplied by the `size` of the hexagon.

        theta : float or int
            Angle (in degrees). Note that the angle is w.r.t to the center. It is not absolute.
            theta can take on 120 degrees, ranging from -30 to + 90, for the point to stay Inside the hexagon


        """

        dist = dist * self.size  # convert fractional distance to hexagonal size units

        if self.verts is None:
            self.verts = self.get_verts()

        pts = []
        for v in range(6):
            pts.append(
                (
                    self.verts[v][0]
                    + dist * sin((-60 * (v + 1) + theta) * PI / 180),  # x
                    self.verts[v][1] + dist * cos((-60 * (v + 1) + theta) * PI / 180),
                )  # y
            )
        return pts

    def get_edge_midpoints(self):
        """Returns 6 points that are in the middle of each of the 6 Edges"""

        if self.flat:
            return self.get_points_dist_from_vertex(0.5, 30)
        else:
            return self.get_points_dist_from_vertex(0.5, 60)

    def get_points_center_rtheta(self, dist, theta_offset, index=None):
        """ Return 6 points that are dist-and angle theta away from the hex center 

        Parameters
        ----------

        dist : float
            distance from the hexagon center, in hexagon-size units. Note: This is not absolute distance. Typically
            `dist` goes from 0 to 1, and gets multiplied by the `size` of the hexagon.

        theta-offset : float or int
            Angle (in degrees). Note that the angle is w.r.t to the center. It is not absolute.

        index: None or integer
            index specifies which spoke or apothem to use for theta offset.
            If index is None, then all 6 are returned

        Returns
        -------
        list
            List of 6 new points, in [(x1,y1), (x2,y2) ...] format

        
        """
        if dist == 0:  # just return the center point
            return (self.x, self.y)

        dist = dist * self.size  # convert fractional distance to hexagonal size units
        theta_offset += 90

        pts = []
        if index is None:
            for v in range(6):
                pts.append(
                    (
                        self.x
                        + dist * sin((-60 * (v + 1) + theta_offset) * PI / 180),  # x
                        self.y + dist * cos((-60 * (v + 1) + theta_offset) * PI / 180),
                    )  # y
                )
        elif index in range(6):
            pts.append(
                (
                    self.x
                    + dist * sin((-60 * (index + 1) + theta_offset) * PI / 180),  # x
                    self.y + dist * cos((-60 * (index + 1) + theta_offset) * PI / 180),
                )  # y
            )
        else:
            print(
                f"Invalid Index {index} specified to function. It must be None or one of 0..5"
            )

        return pts

    def get_points_to_points_rtheta(self, pt, dist_frac, theta_offset, index=None):
        """ Return 6 points that are dist-theta away from the 6 other pts 

        Parameters
        ----------
        pt : list-like or tuple
            pt should have a length of 6 or 1. It should be a list with format
            [(x0,y0), (x1,y1), (x2,y2), (x3,y3), (x4,y4), (x5,y5)] 
            or a tuple (x,y)

        dist_frac : float
            distance from the pt6 points in hexagon height units. Typically a float in (0, 1)

        theta-offset : float or int
            Angle (in degrees). Note that the angle is w.r.t to two points. It is not absolute.

        index: None or integer
            index specifies which spoke or apothem to use for theta offset.
            If index is None, then 6 points are returned

        Returns
        -------
        list
            List of 6 new points, in [(x1,y1), (x2,y2) ...] format
        
            
        """
        inradius = self.ht / 2 if self.flat else self.w / 2
        dist = (
            dist_frac * inradius
        )  # convert fractional distance to hexagonal size units

        if index is None and len(pt) != 6:
            print(f"pt: {pt} Length: {len(pt)}")
            print(
                "Error: Either pt should be 6 points, or Index should be specifed. Index is None."
            )
            return None

        new_pts = []
        if index is None:
            for p in range(6):
                new_pts.append(
                    (
                        pt[p][0]
                        + dist * sin((-60 * (p + 1) + theta_offset) * PI / 180),  # x
                        pt[p][1]
                        + dist * cos((-60 * (p + 1) + theta_offset) * PI / 180),
                    )  # y
                )
                return new_pts
        elif index in range(6):
            return (
                pt[0]
                + dist * sin((-60 * (index) + 150 + theta_offset) * PI / 180),  # x
                pt[1]
                + dist * cos((-60 * (index) + 150 + theta_offset) * PI / 180),  # y
            )
        else:
            print(
                f"Invalid Index {index} specified to function. It must be None or one of 0..5"
            )
            return None

    def point_distance(self, pt):
        """
        Returns the distance from any xy_point to the hexagon

        Parameters
        ----------
        pt : Tuple
            pt should be a tuple (x,y) or [x,y]

        Returns
        -------
        float
            Euclidean Distance from the point pt to the nearest side of the hexagon

        """
        vs = self.get_verts()
        dists = []
        for v in range(6):
            dists.append(point_to_line_dist(pt, vs[v], vs[(v + 1) % 6]))
        return min(dists)

    def render_border(self, ax=None, **kwargs):
        """ Draws all 6 borders of a given Hexagon. fc will color the face."""

        if ax is None:
            ax = plt.gca()

        rot_radians = pi / 6 if self.flat else 0
        polygon = mpatches.RegularPolygon(
            (self.x, self.y),
            numVertices=6,
            radius=self.size,
            orientation=rot_radians,
            **kwargs,
        )
        ax.add_patch(polygon)
        return (ax,)

    def render(self, ax=None, **kwargs):
        """ Draws the edges of a given Hexagon. fc will color the face."""

        if ax is None:
            ax = plt.gca()

        # if self.verts:
        #     vs = self.verts
        # else:
        #     vs = self.get_verts()

        rot_radians = pi / 6 if self.flat else 0
        polygon = mpatches.RegularPolygon(
            (self.x, self.y),
            numVertices=6,
            radius=self.size,
            orientation=rot_radians,
            **kwargs,
        )
        ax.add_patch(polygon)
        return (ax,)

    def v_connect(self, v_pairs, ax=None, **kwargs):
        """ Draws edges from specific vertices to specified vertices.
        
        Parameters
        ----------
        v_pairs: List of tuples of integers
            [vi, vj] where vi and vj are in [0..5] or [(vi0, vj0), (vi1, vj1) ... ]

        Returns
        -------
        None
            One or more Line2D lines connecting pairs of hexagon vertices

        
        """

        if ax is None:
            ax = plt.gca()

        if self.verts is None:
            self.verts = self.get_verts()

        # if just one set of verts are to be connected [1,3] or [[1,3]] are both acceptable.
        # Accounting for that
        if isinstance(v_pairs[0], int):
            v_pairs = [v_pairs]

        # for each vp in v_pairs, connect vi to vj by drawing a Line2D
        for i, j in v_pairs:
            # print(i, j)
            # plot this line for this hexagon
            if not (i in range(6)) and (j in range(6)):
                raise ValueError(f"invalid vertex value specified {(i,j)}")

            x_arr = [self.verts[i][0], self.verts[j][0]]
            y_arr = [self.verts[i][1], self.verts[j][1]]
            edge = Line2D([x_arr], [y_arr], **kwargs)
            ax.add_line(edge)
        return (ax,)

    def connect_pt_to_vertices(self, pt, ax=None, **kwargs):
        """ Draws 'spokes' from a given point to all 6 vertices
        
            pt is a xy tuple
            It usually is, but doesn't have to be inside the hexagon

        """

        if ax is None:
            ax = plt.gca()

        if self.verts is None:
            self.verts = self.get_verts()

        for v in self.verts:
            x_arr = [v.x, pt[0]]
            y_arr = [v.y, pt[1]]
            edge = Line2D([x_arr], [y_arr], **kwargs)
            ax.add_line(edge)
        return (ax,)

    def render_spokes(self, index=None, ax=None, **kwargs):
        """ Draws spokes from center to specific vertices 
        
        
        Parameters
        ----------
        index: None or integer
            index specifies which vertex to use when drawing the spoke
            If index is None, then all 6 spokes are drawn

        Returns
        -------
        None
            One or more spokes are drawn as Line2D lines.

        """

        if ax is None:
            ax = plt.gca()

        if index is None:
            index = range(6)

        if self.verts is None:
            self.verts = self.get_verts()

        # for each v in vlist, connect v to the center by drawing a Line2D
        for v in index:
            x_arr = [self.verts[v][0], self.x]
            y_arr = [self.verts[v][1], self.y]
            edge = Line2D([x_arr], [y_arr], **kwargs)
            ax.add_line(edge)
        return (ax,)

    def render_apothems(self, index=None, ax=None, **kwargs):
        """ Draws spokes from center to specific vertices"""

        if ax is None:
            ax = plt.gca()

        inradius = self.ht / 2 if self.flat else self.w / 2
        pts = self.get_points_center_rtheta(inradius, 120)
        if index in range(6):
            xp, yp = pts[index]
            x_arr = [xp, self.x]
            y_arr = [yp, self.y]
        else:  # draw all six
            # for each pt connect v to the center by drawing a Line2D
            for pt in pts:
                x_arr = [pt[0], self.x]
                y_arr = [pt[1], self.y]
        edge = Line2D([x_arr], [y_arr], **kwargs)
        ax.add_line(edge)
        return (ax,)

    def render_regular_polygon_from_center(
        self, polygon_sides, polygon_size=None, angle_radians=None, ax=None, **kwargs
    ):
        """ Draws a regular polygon that shares its center with hexagon

            Useful for drawing polygon _within_ the existing hexagonal space. For example, smaller hexagons inside the main grid.
        
            Parameters
            =========== 

            polygon_sides = number of sides in the regular polygon

            polygon_size = Size of the polygon's side to be drawn. (defaults to hexagon's size)
            angle_radians = will rotate the regular polygon by radians angle
            fc:  will color the face

        """

        if ax is None:
            ax = plt.gca()

        if polygon_size is None:
            polygon_size = self.size

        if angle_radians is None:
            angle_radians = 0
            if polygon_sides == 6 and self.flat:
                angle_radians = pi / 6

        polygon = mpatches.RegularPolygon(
            (self.x, self.y),
            numVertices=polygon_sides,
            radius=polygon_size,
            orientation=angle_radians,
            **kwargs,
        )
        ax.add_patch(polygon)
        return (ax,)

    def render_polygon(self, pt_list, include_center=False, ax=None, **kwargs):
        """ Draw a Polygon to connect specific vertices and optionally center
        
        
        Parameters:
        
        include_center: Boolean
            Indicates whether the Center of the hexagon should to a vertex of the Polygon being rendered
            Default: False

        pt_list: List
            A list of Integers (0..5) or (x,y) coordinates. Note that this must start and end at the same 
            point to 'complete' the polygon to be drawn
            
        
        """

        if ax is None:
            ax = plt.gca()

        if self.verts is None:
            self.verts = self.get_verts()

        # Make a polygon of all the pts in pt_list
        xy_arr = []
        if include_center:
            xy_arr.append([self.x, self.y])

        # if len(pt_list):
        #     if pt_list[0] in range(6) and (pt_list[0] != pt_list[-1]):
        #         print("Warning: pt_list cannot form a complete Polygon. Please check")

        for pt in pt_list:
            if pt in range(6):  # v is one of the vertices
                xy_arr.append([self.verts[pt][0], self.verts[pt][1]])
            else:
                xy_arr.append(pt)  # pt must be of format (x,y)

        polygon = Polygon(xy_arr, closed=True, **kwargs)
        ax.add_patch(polygon)

        return (ax,)

    def render_circle(self, incircle=True, ax=None, **kwargs):
        """ Draw the incircle with raduis equal to the apothem of the hexagon
        
        Parameters
        ----------
        
        incircle: Boolean, optional
            If True, indicates that the incircle should be rendered. If False, indicates that the circumcircle should be rendered. Default is True.

        """

        if ax is None:
            ax = plt.gca()

        if incircle:
            radius = self.ht / 2 if self.flat else self.w / 2
        else:
            radius = self.size

        hcircle = Circle((self.x, self.y), radius, **kwargs)
        ax.add_patch(hcircle)

    def render_arc(self, incircle=True, ax=None, **kwargs):
        """ Draw the incircle with raduis equal to the apothem of the hexagon
        
        Parameters
        ----------
        
        incircle: Boolean, optional
            If True, indicates that the incircle should be rendered
            If False, indicates that the circumcircle should be rendered
            Default is True.

        """

        if ax is None:
            ax = plt.gca()

        if incircle:
            radius = self.ht if self.flat else self.w
        else:
            radius = self.size * 2

        h_arc = Arc((self.x, self.y), width=radius, height=radius, **kwargs)
        ax.add_patch(h_arc)

    def render_parallel_line(self, edge_name, dist_frac, **kwargs):
        """ Draws a Line parallel to a named edge at the specified distance """

        if edge_name in EDGE_NUM:
            edgenum = int(edge_name[-1])
            start_e = "e" + str((edgenum - 1) % 6)
            end_e = "e" + str((edgenum + 1) % 6)
        else:
            raise Exception(f"Edge_name should be one of {EDGE_NUM}, not {edge_name}.")

        self.line(
            start_point=start_e,
            end_point=end_e,
            start_pos=1 - dist_frac,
            end_pos=dist_frac,
            **kwargs,
        )

    def render_line(self, pts, close=False, ax=None, **kwargs):
        """ 
        Connects all specified pts (xy) by drawing lines between them, sequentially 
        
        Parameters
        ----------
        
        pts: List-like set of xy tuples
            [(x0,y0), (x1,y1), (x2,y2),...]

        close: Boolean, optional
            A flag to specify if the last point should be connected to the first one via a line. Default 
            is False.

        """

        if ax is None:
            ax = plt.gca()

        if close:  # connect pt0 with pt_N
            pts.append(pts[0])

        # add a line between each pair
        for i in range(len(pts) - 1):
            x_arr, y_arr = [], []
            x_arr.append(pts[i][0])
            x_arr.append(pts[i + 1][0])
            y_arr.append(pts[i][1])
            y_arr.append(pts[i + 1][1])
            edge = Line2D([x_arr], [y_arr], **kwargs)
            ax.add_line(edge)

        return (ax,)

    def draw_axis(self, orient="x", **kwargs):
        """ Draw a line from one vertex to its opposite vertex, of speicified orientation
        
        Parameters
        ----------
        orient: str, optional
            Valid values are "x", "y", or "z." Default is "x"
        """

        if orient in ["x", "X"]:
            if not self.flat:
                self.v_connect([1, 4], **kwargs)
            else:
                self.v_connect([0, 3], **kwargs)
        if orient in ["y", "Y"]:
            if not self.flat:
                self.v_connect([0, 3], **kwargs)
            else:
                self.v_connect([2, 5], **kwargs)
        if orient in ["z", "Z"]:
            if not self.flat:
                self.v_connect([2, 5], **kwargs)
            else:
                self.v_connect([1, 4], **kwargs)

    def draw_xaxis(self, **kwargs):
        """ Draw x-axis for a given hexagon """
        self.draw_axis(orient="x", **kwargs)

    def draw_yaxis(self, **kwargs):
        """ Draw y-axis for a given hexagon """
        self.draw_axis(orient="y", **kwargs)

    def draw_zaxis(self, **kwargs):
        """ Draw z-axis for a given hexagon """
        self.draw_axis(orient="z", **kwargs)

    def plot_points(self, pts, **kwargs):
        """ Draws all the pts (xy) specified """

        if not "color" in kwargs:
            kwargs["color"] = "k"

        try:
            for p in pts:
                plt.scatter(*p, s=50, **kwargs)
        except:  # single point, just plot it without looping
            plt.scatter(*pts, s=50, **kwargs)

    def draw_symmetrical_lines(
        self,
        lattice_tup,
        axis,
        color_scheme={},
        close=False,
        connect_original_points=True,
        draw_axis=False,
        **kwargs,
    ):
        """
        Draw pairs of lines connecting the given points across the specified axis. 
        
        By default, it will draw the line connecting the original set of points as well. 
        
        Parameters
        ------------
        
        lattice_tup: tuple
            This tuple is made up of a `pt_name` and an `index` specifying the lattice point uniquely.
            pt_name: string. A special name to denote specific lattice points. Allowable values are:
            ['sa', 'sb', 'ea', 'eb', 'ab']
            
            index: integer  index specifies which spoke or apothem to use for theta offset. Valid values are 
            integers from 0..5

        axis: string, optional
            The Axis of reflective symmetry. Should be one of 'x', 'y', 'z', or '6'.


        color_scheme: Dict, optional
            Specifies which colors to use for the original and reflected lines. Keys can only 'x', 'y', 'z' or '6'
            The value of the dictionary should be a List of color names. It should be 1, 2, or 6 colors for 6-fold
            symmetry. If only one color is specified, then all lines will be drawn with that color.
            
        close: Boolean, optional
            A flag to specify if the last point should be connected to the first one via a line. Default 
            is False.

        Returns
        -------
        None
            One or more spokes are drawn as Line2D lines.
        
        """

        axis = axis.lower()
        if axis not in ["x", "y", "z", "6"]:
            raise ValueError(f"faulty axis specified for reflection")

        if self.lattice is None:
            self.get_lattice_points()

        if close:
            lattice_tup.append(lattice_tup[0])

        pts = [self.lattice[_name][i] for _name, i in lattice_tup]
        pt_indices = [i for _name, i in lattice_tup]

        sympts = []
        for ptup in lattice_tup:
            sympt = self.get_symmetrical_point(ptup, axis)
            sympts.append(sympt)

        if axis == "6":
            # requires delicated ops. Take the sets 2 at a time, and for every pair, connect them
            for i in range(0, len(sympts) - 1):
                # offset is the difference between every 2 adjacent indices of the hex segments
                offset = pt_indices[i + 1] - pt_indices[i]
                for petal in range(6):  # we will draw 6 symmetrical segments...
                    if axis in color_scheme:
                        if len(color_scheme[axis]) >= 6:
                            kwargs["color"] = color_scheme[axis][petal]
                        else:  # just use the first color alone
                            kwargs["color"] = color_scheme[axis][0]
                    self.render_line(
                        [sympts[i][petal], sympts[i + 1][(petal + offset) % 6]],
                        close=close,
                        **kwargs,
                    )

        else:  # for x y or z reflections

            # Draw the original Line(s)
            if axis in color_scheme:
                kwargs["color"] = color_scheme[axis][0]
            self.render_line(pts, close=close, **kwargs)

            # Draw the reflected Line(s)
            if (
                axis in color_scheme and len(color_scheme[axis]) > 1
            ):  # there is a second color
                kwargs["color"] = color_scheme[axis][1]
            self.render_line(sympts, close=close, **kwargs)

        # self.plot_points(pts)# close=False, color='r', **kwargs)
        if draw_axis:
            self.draw_axis(axis, **kwargs)

    def decorate(self, poly=None, line=None, include_center=True, ax=None, **kwargs):
        """ Draw a Polygon to connect specific vertices and optionally center
        
        
        Parameters
        ----------

        """

        if poly is not None:
            if poly not in ALLOWABLE_POLYGONS:
                print(f"poly {poly} is not defined.")
            else:
                self.render_polygon(
                    pt_list=poly, include_center=include_center, **kwargs
                )

    def point(
        self, pt_name, action=None, index=None, dist=None, theta=None, ax=None, **kwargs
    ):
        """ Return one or six points in the hexagon based on specifications.
        
        
        Parameters
        ----------

        pt-name: string
            Name of the point type desired: Allowable values are `center`, `vertex`, `vertices`, 
            `spokes`, `edge(s)`, `apo|them`

        dist : float
            distance from the hexagon center, in hexagon-size units. Note: This is not absolute distance. Typically
            `dist` goes from 0 to 1, and gets multiplied by the `in-radius` of the hexagon.

        theta: float or int
            Angle (in degrees). 

        index: None or integer
            index specifies which spoke or apothem to use for theta offset.
            If index is None, then all 6 are returned

        Returns
        -------
        List of 6 new points, in [(x1,y1), (x2,y2) ...] format
            If `index` is specified, then only one point is returned
    
        
        """

        if pt_name == "center":
            if dist == "random" or (dist is None):
                dist = np.random.random()

            if theta is None:
                theta = np.random.randint(60)

            return self.get_points_center_rtheta(dist, theta_offset=theta, index=index)

        if self.verts is None:
            self.verts = self.get_verts()

        if pt_name in ["verts", "vertices", "vertex"]:

            if dist == "random" or (dist is None):
                dist = np.random.random()

            if theta is None:
                theta = np.random.randint(60)
            return self.get_points_dist_from_vertex(dist, theta)

        if pt_name in ["edge", "edges", "e"]:
            if action == "trisect":
                set1 = self.get_points_on_edge(edge=index, dist_frac=1 / 3)
                set2 = self.get_points_on_edge(edge=index, dist_frac=2 / 3)
                return list(set1 + set2)
            elif action is None:
                if dist == "random" or (dist is None):
                    dist = np.random.random()

                return self.get_points_on_edge(edge=index, dist_frac=dist)

        if pt_name in ["spoke", "spokes", "apothem", "apo"]:
            inradius = self.ht / 2 if self.flat else self.w / 2

            if pt_name in ["spoke", "spokes"]:
                theta_offset = 60
            else:  # apothem
                theta_offset = 30

            if action == "bisect":
                if pt_name in ["spoke", "spokes"]:
                    dist = 1 / 2
                else:  # apothem
                    dist = 1 / 2 * inradius / self.size
                return self.get_points_center_rtheta(dist, theta_offset)

            if action == "trisect":
                if pt_name in ["spoke", "spokes"]:
                    triseg = 1 / 3
                else:  # apothem
                    triseg = 1 / 3 * inradius / self.size

                set1 = self.get_points_center_rtheta(
                    dist=triseg, theta_offset=theta_offset
                )
                set2 = self.get_points_center_rtheta(
                    dist=triseg * 2, theta_offset=theta_offset
                )
                return list(set1 + set2)

            if dist == "random" or (dist is None):
                if pt_name in ["spoke", "spokes"]:
                    dist = self.size * np.random.random()
                else:  # apothem
                    inradius = self.ht / 2 if self.flat else self.w / 2
                    dist = inradius * np.random.random()

            return self.get_points_center_rtheta(dist, theta_offset, index)

    def line(
        self,
        start_point,
        end_point,
        start_pos=None,
        end_pos=None,
        index=None,
        line_len=None,
        theta=None,
        ax=None,
        **kwargs,
    ):
        """ Draw one or multiple lines in the hexagon based on specifications.
                
        Parameters
        ----------

        start_point: string
            Name of the point type desired: Allowable values are `center`, `vertex`, `vertices`, 
            `edge(s)`, `random`, 'e1' ...'e5' or 'v1'...'v5

        end_point: string
            Name of the point type desired: Allowable values are `center`, `vertex`, `vertices`, 
            `edge(s)`, `random`, 'e1' ...'e5' or 'v1'...'v5

        dist : float
            distance from the hexagon center, in hexagon-size units. Note: This is not absolute distance. Typically
            `dist` goes from 0 to 1, and gets multiplied by the `in-radius` of the hexagon.

        theta: float or int
            Angle (in degrees). 

        index: None or integer
            index specifies which spoke or apothem to use for theta offset.
            If index is None, then all 6 are returned

        Returns
        -------
        None: None
            The line(s) get plotted, so nothing is returned
    
        
        """
        if ax is None:
            ax = plt.gca()

        if start_point == "center" and end_point in VERT_NAMES:  # one of more spokes
            if end_point not in VERT_NUM:  # draw all spokes
                self.render_spokes()
            else:
                try:
                    v_index = []
                    v_index.append(int(end_point[-1]))
                except:
                    print(end_point, type(end_point))
                    print(int(end_point[-1]))
                    print(
                        f"end_point specification incorrect. Should be one of {VERT_NUM}"
                    )
                self.render_spokes(index=v_index)

        if start_point in EDGE_NAMES:
            if end_point in EDGE_NAMES:
                st_edge, end_edge = -1, -1
                while st_edge == end_edge:
                    st_edge = _determine_edge(start_point)
                    end_edge = _determine_edge(end_point)
                    # add a circuit breaker
                stpos = _determine_position(start_pos)
                endpos = _determine_position(end_pos)
                st = self.point(pt_name="edge", dist=stpos, index=st_edge)[0]
                end = self.point(pt_name="edge", dist=endpos, index=end_edge)[0]
                eeline = Line2D([st[0], end[0]], [st[1], end[1]], **kwargs)
                ax.add_line(eeline)
                return (ax,)


def _determine_position(pos):
    if pos is None or pos in ["random", "rnd", "rand"]:
        return np.random.random()
    if pos == "mid":
        return 0.5
    if pos in ["med", "medium"]:
        return np.random.uniform(0.33, 0.66)
    if pos in ["near", "low"]:
        return np.random.uniform(0, 0.33)
    if pos in ["high", "far"]:
        return np.random.uniform(0.66, 1)
    if isinstance(pos, (int, float)):
        return pos
    else:
        print(f"{pos} is not a valid Position argument")
        return None


def _determine_edge(pt_name):
    if pt_name not in EDGE_NAMES:
        print(f"{pt_name} is not a valid Edge reference")
        return None
    if pt_name in EDGE_NUM:
        return int(pt_name[-1])
    else:  # random
        return np.random.randint(6)


# https://stackoverflow.com/questions/27161533/find-the-shortest-distance-between-a-point-and-line-segments-not-line
def point_to_line_dist(pt, line_seg_endpoint1, line_seg_endpoint2):
    """Calculate the distance between a point and a line segment.

    To calculate the closest distance to a line segment, we first need to check
    if the point projects onto the line segment.  If it does, then we calculate
    the orthogonal distance from the point to the line.
    If the point does not project to the line segment, we calculate the 
    distance to both endpoints and take the shortest distance.

    :param point: Numpy array of form [x,y], describing the point.
    :type point: numpy.core.multiarray.ndarray
    :param line: list of endpoint arrays of form [P1, P2]
    :type line: list of numpy.core.multiarray.ndarray
    :return: The minimum distance to a point.
    :rtype: float
    """

    point = np.array(pt)
    line = np.array(
        [
            [line_seg_endpoint1[0], line_seg_endpoint1[1]],
            [line_seg_endpoint2[0], line_seg_endpoint2[1]],
        ]
    )

    # unit vector
    unit_line = line[1] - line[0]
    norm_unit_line = unit_line / np.linalg.norm(unit_line)

    # compute the perpendicular distance to the theoretical infinite line
    segment_dist = np.linalg.norm(
        np.cross(line[1] - line[0], line[0] - point)
    ) / np.linalg.norm(unit_line)

    diff = (norm_unit_line[0] * (point[0] - line[0][0])) + (
        norm_unit_line[1] * (point[1] - line[0][1])
    )

    x_seg = (norm_unit_line[0] * diff) + line[0][0]
    y_seg = (norm_unit_line[1] * diff) + line[0][1]

    endpoint_dist = min(
        np.linalg.norm(line[0] - point), np.linalg.norm(line[1] - point)
    )

    # decide if the intersection point falls on the line segment
    lp1_x = line[0][0]  # line point 1 x
    lp1_y = line[0][1]  # line point 1 y
    lp2_x = line[1][0]  # line point 2 x
    lp2_y = line[1][1]  # line point 2 y
    is_betw_x = lp1_x <= x_seg <= lp2_x or lp2_x <= x_seg <= lp1_x
    is_betw_y = lp1_y <= y_seg <= lp2_y or lp2_y <= y_seg <= lp1_y
    if is_betw_x and is_betw_y:
        return segment_dist
    else:
        # if not, then return the minimum distance to the segment endpoints
        return endpoint_dist


class HexGrid:

    """Represents the a hexagonal grid as painted on the screen.
    The hex grid can be flat topped (flat = True) or pointy-topped (flat=False)
    
    It has a list of hexs in hlist
    And there is a rectangle (a bounding box) for the grid, since it has to be rendered in the xy plane
    
    """

    def __init__(
        self,
        num_rows,
        num_cols,
        size=1,
        flat=True,
        xstart=0,
        ystart=0,
        rect_h=None,
        rect_w=None,
    ):

        self.num_rows = num_rows
        self.num_cols = num_cols
        self.size = size
        self.flat = flat
        self.hlist = []
        self.centers = []

        if flat:
            hexh = sqrt(3) * size
            hexw = 2 * size
            xdist = 3 / 2 * hexw
            ydist = hexh / 2
        else:
            hexw = sqrt(3) * size
            hexh = 2 * size
            ydist = 3 / 4 * hexh
            xdist = hexw

        id = 0
        for row in range(num_rows):
            if flat:
                x_from_left = (3 / 4 * hexw if row % 2 else 0) - ((num_cols + 1) * size)
                y_from_bottom = -1 * hexh * (num_rows // 4)
            else:
                x_from_left = (0 if row % 2 else hexw / 2) - (num_cols // 2 * hexw)
                y_from_bottom = -1 * (hexh * (num_rows // 2)) + (
                    size * (num_rows // 2 - 1)
                )

            for col in range(num_cols):
                cx, cy = (
                    xstart + x_from_left + col * xdist,
                    ystart + ydist * row + y_from_bottom,
                )
                # c = Point(cx, cy)
                hx = Hex(
                    cx, cy, size, id=id, flat=flat
                )  # instantiate Hex based on center and size
                hx.row, hx.col = row, col

                # xyz cube coords get assigned during __init__
                if flat:
                    hx.xc = (
                        (col * 2) + (row % 2) - (num_cols)
                    )  # same for a col, increases by 1 when  col increases
                    hx.zc = (
                        (num_rows // 2) + 1 - (row) - (col) + (row // 2)
                    )  # decreases with row. start with a big value
                    hx.yc = (hx.xc + hx.zc) * (-1)
                else:  # pointy Cube coords
                    hx.xc = row // 2 + col - (num_cols // 2) - 2
                    hx.zc = (num_rows // 2) - row
                    hx.yc = (hx.xc + hx.zc) * (-1)

                hx.get_verts()
                self.hlist.append(hx)
                self.centers.append((cx, cy))
                id += 1

    def __str__(self):
        desc = "Flat" if self.flat else "Pointy"
        str1 = f" HexGrid: {len(self.centers)} {desc}-hexagons {self.num_rows} by {self.num_cols} of size {self.size}\n"
        return str1

    def render_grid(self, **kwargs):

        for h in self.hlist:
            h.render(**kwargs)

    def render_grid_vconnect(self, v_pairs=None, **kwargs):
        """ For entire HexGrid connect vert to vert without necessarily going through the center"""

        if v_pairs is not None:
            for h in self.hlist:
                h.v_connect(v_pairs, **kwargs)

    def render_grid_spokes(self, c_to_vlist=None, **kwargs):
        """ For entire HexGrid connect center to specified vertices"""
        if c_to_vlist is not None:
            for h in self.hlist:
                h.render_spokes(c_to_vlist, **kwargs)

    def render_grid_polygons(self, pt_list=None, **kwargs):
        """ For entire HexGrid connect center to vlist"""

        # connect from hex center to each of the specified vertices
        if pt_list is not None:
            for h in self.hlist:
                h.render_polygon(pt_list, **kwargs)

    def render_grid_vertices(self, **kwargs):
        for h in self.hlist:
            for v in h.verts[:3]:
                plt.scatter(v.x, v.y, **kwargs)

                plt.scatter(h.x, h.y, **kwargs)


def get_hexgrid_centers(hg):
    """ get the center x and y coords for each hexagon as a list of (x,y)"""
    return [(h.x, h.y) for h in hg.hlist]

