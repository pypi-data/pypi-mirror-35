"""
points.py
-------------

Functions dealing with (n,d) points.
"""
import numpy as np

from .constants import tol
from .geometry import plane_transform

from . import util
from . import caching
from . import grouping
from . import transformations


def point_plane_distance(points,
                         plane_normal,
                         plane_origin=[0.0, 0.0, 0.0]):
    """
    The minimum perpendicular distance of a point to a plane.

    Parameters
    -----------
    points:       (n, 3) float, points in space
    plane_normal: (3,) float, normal vector
    plane_origin: (3,) float, plane origin in space

    Returns
    ------------
    distances:     (n,) float, distance from point to plane
    """
    points = np.asanyarray(points, dtype=np.float64)
    w = points - plane_origin
    distances = np.dot(plane_normal, w.T) / np.linalg.norm(plane_normal)
    return distances


def major_axis(points):
    """
    Returns an approximate vector representing the major axis of points

    Parameters
    -------------
    points: (n, dimension) float, points in space

    Returns
    -------------
    axis: (dimension,) float, vector along approximate major axis
    """
    U, S, V = np.linalg.svd(points)
    axis = util.unitize(np.dot(S, V))
    return axis


def plane_fit(points):
    """
    Given a set of points, find an origin and normal using SVD.

    Parameters
    ---------
    points : (n,3) float
        Points in 3D space

    Returns
    ---------
    C : (3,) float
        Point on the plane
    N : (3,) float
        Normal vector of plane
    """
    # make sure input is numpy array
    points = np.asanyarray(points, dtype=np.float64)
    # make the plane origin the mean of the points
    C = points.mean(axis=0)
    # points offset by the plane origin
    x = points - C
    # create a (3, 3) matrix
    M = np.dot(x.T, x)
    # run SVD
    N = np.linalg.svd(M)[0][:, -1]

    return C, N


def radial_sort(points,
                origin,
                normal):
    """
    Sorts a set of points radially (by angle) around an
    origin/normal.

    Parameters
    --------------
    points: (n,3) float, points in space
    origin: (3,)  float, origin to sort around
    normal: (3,)  float, vector to sort around

    Returns
    --------------
    ordered: (n,3) flot, re- ordered points in space
    """

    # create two axis perpendicular to each other and the normal,
    # and project the points onto them
    axis0 = [normal[0], normal[2], -normal[1]]
    axis1 = np.cross(normal, axis0)
    ptVec = points - origin
    pr0 = np.dot(ptVec, axis0)
    pr1 = np.dot(ptVec, axis1)

    # calculate the angles of the points on the axis
    angles = np.arctan2(pr0, pr1)

    # return the points sorted by angle
    return points[[np.argsort(angles)]]


def project_to_plane(points,
                     plane_normal=[0, 0, 1],
                     plane_origin=[0, 0, 0],
                     transform=None,
                     return_transform=False,
                     return_planar=True):
    """
    Projects a set of (n,3) points onto a plane.

    Parameters
    ---------
    points:           (n,3) array of points
    plane_normal:     (3) normal vector of plane
    plane_origin:     (3) point on plane
    transform:        None or (4,4) matrix. If specified, normal/origin are ignored
    return_transform: bool, if true returns the (4,4) matrix used to project points
                      onto a plane
    return_planar:    bool, if True, returns (n,2) points. If False, returns
                      (n,3), where the Z column consists of zeros
    """

    if np.all(np.abs(plane_normal) < tol.zero):
        raise NameError('Normal must be nonzero!')

    if transform is None:
        transform = plane_transform(plane_origin, plane_normal)

    transformed = transformations.transform_points(points, transform)
    transformed = transformed[:, 0:(3 - int(return_planar))]

    if return_transform:
        polygon_to_3D = np.linalg.inv(transform)
        return transformed, polygon_to_3D
    return transformed


def absolute_orientation(points_A, points_B, return_error=False):
    """
    Calculates the transform that best aligns points_A with points_B
    Uses Horn's method for the absolute orientation problem, in 3D with no scaling.

    Parameters
    ---------
    points_A:     (n,3) list of points
    points_B:     (n,3) list of points, T*points_A
    return_error: boolean, if True returns (n) list of euclidean distances
                  representing the distance from  T*points_A[i] to points_B[i]


    Returns
    ---------
    M:    (4,4) transformation matrix for the transform that best aligns
           points_A to points_B
    error: float, list of maximum euclidean distance
    """

    points_A = np.array(points_A)
    points_B = np.array(points_B)
    if (points_A.shape != points_B.shape):
        raise ValueError('Points must be of the same shape!')
    if len(points_A.shape) != 2 or points_A.shape[1] != 3:
        raise ValueError('Points must be (n,3)!')

    lc = np.average(points_A, axis=0)
    rc = np.average(points_B, axis=0)
    left = points_A - lc
    right = points_B - rc
    M = np.dot(left.T, right)
    [[Sxx, Sxy, Sxz],
     [Syx, Syy, Syz],
     [Szx, Szy, Szz]] = M
    N = [[(Sxx + Syy + Szz), (Syz - Szy), (Szx - Sxz), (Sxy - Syx)],
         [(Syz - Szy), (Sxx - Syy - Szz), (Sxy + Syx), (Szx + Sxz)],
         [(Szx - Sxz), (Sxy + Syx), (-Sxx + Syy - Szz), (Syz + Szy)],
         [(Sxy - Syx), (Szx + Sxz), (Syz + Szy), (-Sxx - Syy + Szz)]]
    (w, v) = np.linalg.eig(N)
    q = v[:, np.argmax(w)]
    q = q / np.linalg.norm(q)
    M1 = [[q[0], -q[1], -q[2], -q[3]],
          [q[1], q[0], q[3], -q[2]],
          [q[2], -q[3], q[0], q[1]],
          [q[3], q[2], -q[1], q[0]]]
    M2 = [[q[0], -q[1], -q[2], -q[3]],
          [q[1], q[0], -q[3], q[2]],
          [q[2], q[3], q[0], -q[1]],
          [q[3], -q[2], q[1], q[0]]]
    R = np.dot(np.transpose(M1), M2)[1:4, 1:4]
    T = rc - np.dot(R, lc)

    M = np.eye(4)
    M[0:3, 0:3] = R
    M[0:3, 3] = T

    if return_error:
        errors = np.sum((transformations.transform_points(
            points_A, M) - points_B)**2, axis=1)
        return M, errors.max()
    return M


def remove_close(points, radius):
    """
    Given an (n, m) set of points where n=(2|3) return a list of points
    where no point is closer than radius.

    Parameters
    ------------
    points: (n, dimension) float, points in space
    radius: float, minimum radius between result points

    Returns
    ------------
    culled: (m, dimension) float, points in space
    mask:   (n,) bool, which points from the original set were returned
    """
    from scipy.spatial import cKDTree as KDTree

    tree = KDTree(points)
    consumed = np.zeros(len(points), dtype=np.bool)
    unique = np.zeros(len(points), dtype=np.bool)
    for i in range(len(points)):
        if consumed[i]:
            continue
        neighbors = tree.query_ball_point(points[i], r=radius)
        consumed[neighbors] = True
        unique[i] = True

    return points[unique], unique


def remove_close_set(points_fixed, points_reduce, radius):
    """
    Given two sets of points and a radius, return a set of points
    that is the subset of points_reduce where no point is within
    radius of any point in points_fixed
    """
    from scipy.spatial import cKDTree as KDTree

    tree_fixed = KDTree(points_fixed)
    tree_reduce = KDTree(points_reduce)
    reduce_duplicates = tree_fixed.query_ball_tree(tree_reduce, r=radius)
    reduce_duplicates = np.unique(np.hstack(reduce_duplicates).astype(int))
    reduce_mask = np.ones(len(points_reduce), dtype=np.bool)
    reduce_mask[reduce_duplicates] = False
    points_clean = points_reduce[reduce_mask]
    return points_clean


def k_means(points, k, **kwargs):
    """
    Find k centroids that attempt to minimize the k- means problem:
    https://en.wikipedia.org/wiki/Metric_k-center

    Parameters
    ----------
    points:  (n, d) float
        Points in a space
    k : int
         Number of centroids to compute
    **kwargs : dict
        Passed directly to scipy.cluster.vq.kmeans

    Returns
    ----------
    centroids : (k, d) float
         Points in some space
    labels: (n) int
        Indexes for which points belong to which centroid
    """
    from scipy.cluster.vq import kmeans
    from scipy.spatial import cKDTree

    points = np.asanyarray(points)
    points_std = points.std(axis=0)
    whitened = points / points_std
    centroids_whitened, distortion = kmeans(whitened, k, **kwargs)
    centroids = centroids_whitened * points_std
    tree = cKDTree(centroids)
    labels = tree.query(points, k=1)[1]
    return centroids, labels


def plot_points(points, show=True):
    """
    Plot an (n,3) list of points using matplotlib.

    """
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    points = np.asanyarray(points)
    dimension = points.shape[1]
    if dimension == 3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(*points.T)
    elif dimension == 2:
        plt.scatter(*points.T)
    else:
        raise ValueError('Points must be 2D or 3D, not %dD', dimension)

    if show:
        plt.show()


class PointCloud(object):
    """
    Hold a 3D set of points in an object which can be visualized
    in a scene.
    """

    def __init__(self, *args, **kwargs):
        self._data = caching.DataStore()
        self.metadata = {}

        if len(args) == 1:
            self.vertices = args[0]

        if 'vertices' in kwargs:
            self.vertices = kwargs['vertices']

        if 'color' in kwargs:
            self.colors = kwargs['color']

    def md5(self):
        return self._data.md5()

    def merge_vertices(self):
        """
        Merge vertices closer than tol.merge (default: 1e-8)
        """
        # run unique rows
        unique, inverse = grouping.unique_rows(self.vertices)

        # apply unique mask to vertices
        self.vertices = self.vertices[unique]

        # apply unique mask to colors
        if (self.colors is not None and
                len(self.colors) == len(inverse)):
            self.colors = self.colors[unique]

    @property
    def bounds(self):
        return np.array([self.vertices.min(axis=0),
                         self.vertices.max(axis=0)])

    @property
    def extents(self):
        return self.bounds.ptp(axis=0)

    @property
    def centroid(self):
        return self.vertices.mean(axis=0)

    @property
    def vertices(self):
        return self._data['vertices']

    @vertices.setter
    def vertices(self, data):
        data = np.asanyarray(data, dtype=np.float64)
        if not util.is_shape(data, (-1, 3)):
            raise ValueError('Point clouds only consist of (n,3) points!')
        self._data['vertices'] = data

    @property
    def colors(self):
        return self._data['colors']

    @colors.setter
    def colors(self, data):
        data = np.asanyarray(data)
        if data.shape == (4,):
            data = np.tile(data, (len(self.vertices), 1))
        self._data['colors'] = data

    def scene(self):
        from .scene.scene import Scene
        return Scene(self)

    def show(self):
        self.scene().show()
