# Source: http://rosettacode.org/wiki/Determine_if_two_triangles_overlap#Python
"""Module to check triangle overlappinng"""

from __future__ import print_function
import numpy as np


def check_triangle_winding(tri, allow_reversed):
    """Check triangle winding"""
    triangle_sq = np.ones((3, 3))
    triangle_sq[:, 0:2] = np.array(tri)
    det_triangle = np.linalg.det(triangle_sq)
    if det_triangle < 0.0:
        if allow_reversed:
            tmp = triangle_sq[2, :].copy()
            triangle_sq[2, :] = triangle_sq[1, :]
            triangle_sq[1, :] = tmp
        else:
            raise ValueError("Triangle has wrong winding direction")
    return triangle_sq


def compare_triange_to_triange_2dim(tri_1, tri_2, eps=0.0, allow_reversed=False, on_boundary=True):
    """Triangle to triangle in 2 dimentional space"""
    # Trangles must be expressed anti-clockwise
    tri_1_s = check_triangle_winding(tri_1, allow_reversed)
    tri_2_s = check_triangle_winding(tri_2, allow_reversed)

    if on_boundary:
        # Points on the boundary are considered as colliding
        check_edge = lambda x: np.linalg.det(x) < eps
    else:
        # Points on the boundary are not considered as colliding
        check_edge = lambda x: np.linalg.det(x) <= eps

    # For edge E of trangle 1,
    for i in range(3):
        edge = np.roll(tri_1_s, i, axis=0)[:2, :]

        # Check all points of trangle 2 lay on the external side of the edge E. If
        # they do, the triangles do not collide.
        if (check_edge(np.vstack((edge, tri_2_s[0]))) and
                check_edge(np.vstack((edge, tri_2_s[1]))) and
                check_edge(np.vstack((edge, tri_2_s[2])))):
            return False

    # For edge E of trangle 2,
    for i in range(3):
        edge = np.roll(tri_2_s, i, axis=0)[:2, :]

        # Check all points of trangle 1 lay on the external side of the edge E. If
        # they do, the triangles do not collide.
        if (check_edge(np.vstack((edge, tri_1_s[0]))) and
                check_edge(np.vstack((edge, tri_1_s[1]))) and
                check_edge(np.vstack((edge, tri_1_s[2])))):
            return False

    # The triangles collide
    return True


if __name__ == "__main__":
    triangle_1 = [[0, 0], [5, 0], [0, 5]]
    triangle_2 = [[0, 0], [5, 0], [0, 6]]
    print(compare_triange_to_triange_2dim(triangle_1, triangle_2), True)

    triangle_1 = [[0, 0], [0, 5], [5, 0]]
    triangle_2 = [[0, 0], [0, 6], [5, 0]]
    print(compare_triange_to_triange_2dim(triangle_1, triangle_2, allow_reversed=True), True)

    triangle_1 = [[0, 0], [5, 0], [0, 5]]
    triangle_2 = [[-10, 0], [-5, 0], [-1, 6]]
    print(compare_triange_to_triange_2dim(triangle_1, triangle_2), False)

    triangle_1 = [[0, 0], [5, 0], [2.5, 5]]
    triangle_2 = [[0, 4], [2.5, -1], [5, 4]]
    print(compare_triange_to_triange_2dim(triangle_1, triangle_2), True)

    triangle_1 = [[0, 0], [1, 1], [0, 2]]
    triangle_2 = [[2, 1], [3, 0], [3, 2]]
    print(compare_triange_to_triange_2dim(triangle_1, triangle_2), False)

    triangle_1 = [[0, 0], [1, 1], [0, 2]]
    triangle_2 = [[2, 1], [3, -2], [3, 4]]
    print(compare_triange_to_triange_2dim(triangle_1, triangle_2), False)

    # Barely touching
    triangle_1 = [[0, 0], [1, 0], [0, 1]]
    triangle_2 = [[1, 0], [2, 0], [1, 1]]
    print(compare_triange_to_triange_2dim(triangle_1, triangle_2, on_boundary=True), True)

    # Barely touching
    triangle_1 = [[0, 0], [1, 0], [0, 1]]
    triangle_2 = [[1, 0], [2, 0], [1, 1]]
    print(compare_triange_to_triange_2dim(triangle_1, triangle_2, on_boundary=False), False)
