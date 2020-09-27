"""
Christopher Kramer

Functional implementation of divide-and-conquer algorithm for finding the shortest distance between list containing
1-dimensional integers from the number line.

additional inspiration from:
https://sites.cs.ucsb.edu/~suri/cs235/ClosestPair.pdf
"""

from math import inf
from operator import sub, floordiv, eq
from typing import List, Tuple

# typehints
UnsortedPointList = List[int]
SortedPointList = Tuple[int, ...]
Pair = Tuple[int, int]
MinDistance = int
Distance = int


def cPairDist(points: UnsortedPointList) -> MinDistance:
    return recCPairDist(tuple(sorted(points)))


def recCPairDist(points: SortedPointList) -> MinDistance:
    """
    Min distance algorithm.
    P = sorted list of integers
    recCPairDist(P):
    1. If length(P) = 1:
    2.      return \infty
    3. If length(P) = 2:
    4.      return |p_2 - p_1|
    5. Else:
    6.      Set d_1 <- recCPairDist(P[:median(P)])
    7.      Set d_2 <- recCPairDist(P[median(P):])
    8.      Set d_12 <- |P[median(P)] - P[median(P)-1]|
    9.      return minimum(d_1, d_2, d_12)
    :param points:
    :return: distance
    """
    def pair_subtraction(paired_points: Pair) -> Distance:
        """
        Returns |p_1 - p_2|
        :param paired_points:
        :return:
        """
        return abs(sub(paired_points[1], paired_points[0]))

    def distance_recursion(points: SortedPointList) -> Distance:
        """
        Returns returns min(d_1, d_2, d_12) where d_1, d_2 is the distance between points in two paired lists,
        and d_12 is the distance between the end and beginning of d_1, d_2
        :param points:
        :return:
        """
        m = floordiv(len(points), 2)
        return min(recCPairDist(points[:m]), recCPairDist(points[m:]), pair_subtraction((points[m], points[m - 1])))

    # noinspection PyTypeChecker
    return inf if eq(len(points), 1) else distance_recursion(points)
    #  Don't need this:
    #  else pair_subtraction(points) if eq(len(points), 2)
