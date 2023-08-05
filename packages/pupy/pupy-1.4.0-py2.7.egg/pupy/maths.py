#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from __future__ import division, print_function
from collections import Counter
from math import pi, sqrt, acos, factorial
from operator import floordiv, methodcaller, truediv, add, sub
from pupy.decorations import cash_it
from pupy.listless import iter_product

def partitions_gen(numero, min_p=1, max_p=None):
    """Partitions generator

    Adapted from:
        code.activestate.com/recipes/218332-generator-for-integer-partitions/
        Adaptions:
            min_p: minimum partition value

    Args:
        numero (int): number for which to yield partiton tuples
        min_p (int): smallest part size
        max_p (int): largest part size

    Yields:
        tuple: partition of max_p with smallest partition being min_p

    Examples:
        >>> list(partitions_gen(4))
        [(4,), (1, 3), (1, 1, 2), (1, 1, 1, 1), (2, 2)]
        >>> list(partitions_gen(4, min_p=1, max_p=2))
        [(1, 1, 2), (1, 1, 1, 1), (2, 2)]
    """
    if max_p is None or max_p >= numero:
        yield (numero,)

    for i in range(min_p, numero // 2 + 1):
        for p in partitions_gen(numero - i, i, max_p):
            yield (i,) + p

@cash_it
def rfactorial(n):
    """Recursive factorial function

    Args:
        n:

    Returns:

    """
    if n == 1:
        return 1
    else:
        return rfactorial(n - 1) * n

def radians_2_degrees(rads):
    """Converts radians to degrees"""
    return 180 * rads / pi

def degrees_2_radians(degs):
    """Converts degrees to radians"""
    return degs * pi / 180

def power_mod(number, exponent, mod):
    """

    Args:
        number:
        exponent:
        mod:

    Returns:

    """
    if exponent > 0:
        if exponent % 2 == 0:
            return power_mod(number, floordiv(exponent, 2), mod)
        return power_mod(number, floordiv(exponent, 2), mod) * number
    else:
        return 1

def divisors_gen(n):
    """Divisors generator

    Args:
        n (int): number w/ divisors to be generated

    Yields:
        int: divisors

    """
    large_divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor

def gcd_it(a, b):
    """iterative gcd"""
    while a:
        a, b = b % a, a
    return b

@cash_it
def gcd_r(a, b):
    """recursive greatest common divisor"""
    if b > a:
        return gcd_r(b, a)
    r = a % b
    if r == 0:
        return b
    return gcd_r(r, b)

def reverse(n):
    """Reverses a number

    Args:
        n (int): number to be reversed

    Returns:
        int: reversed of a number

    """

    reversed = 0
    while n > 0:
        reversed *= 10
        reversed += n % 10
        n //= 10
    return reversed

@cash_it
def fib_r(n):
    """Recursively the nth fibonacci number

    Args:
        n (int): nth fibonacci sequence number

    Returns:
        int: the nth fibonacci number

    Examples:
        >>> fib_r(1)
        1
        >>> fib_r(2)
        2
        >>> fib_r(6)
        13
    """
    return n if n < 3 else fib_r(n - 1) + fib_r(n - 2)

def expo(d, n):
    """greatest exponent for a divisor of n

    Args:
        d (int): divisor
        n (int): number be divided

    Returns:
        int: number of times a divisor divides n
    """
    if n < d:  # flip
        d, n = n, d
    c = n
    divs = 0
    while c % d == 0:
        c //= d
        divs += 1
    return divs

def pytriple_gen(max_c):
    """primative pythagorean triples generator

    special thanks to 3Blue1Brown's video on pythagorean triples
    https://www.youtube.com/watch?v=QJYmyhnaaek&t=300s

    Args:
        max_c (int): max value of c to yeild triples up to

    Yields:
        tuple: pythagorean triple (a, b, c)
    """
    for real_pts in range(2, int(sqrt(max_c)) + 1, 1):
        for imag_pts in range(real_pts % 2 + 1, real_pts, 2):
            comp = complex(real_pts, imag_pts)
            sqrd = comp * comp
            real = int(sqrd.real)
            imag = int(sqrd.imag)
            if abs(real - imag) % 2 == 1 and gcd_it(imag, real) == 1:
                sea = int((comp * comp.conjugate()).real)
                if sea > max_c:
                    break
                else:
                    yield (imag, real, sea) if real > imag else (real, imag, sea)

def repermutations(toop):
    c = Counter(n for n in toop)
    a = list(factorial(nc) for nc in c.values())
    ans = factorial(len(toop)) // iter_product(a)
    return ans

def disjoint(a, b):
    return not any(ae in b for ae in a)

def n_choose_r(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)

def pytriple_gen_2():
    diagonal_size = 3
    cur_x = 1
    cur_y = 2
    while True:
        if cur_y <= cur_x:
            diagonal_size += 1
            cur_x = 1
            cur_y = diagonal_size - 1
        imag_part = cur_y
        real_part = cur_x
        to_yield = get_pythag_triple(real_part, imag_part)
        cur_x += 1
        cur_y -= 1
        if gcd_it(to_yield[0], to_yield[1]) > 1:
            continue
        yield to_yield

def get_pythag_triple(real, imag):
    comp = complex(real, imag)
    sea = int((comp * comp.conjugate()).real)
    sqrd = comp * comp
    real = abs(int(sqrd.real))
    imag = abs(int(sqrd.imag))
    return min(imag, real), max(imag, real), sea

class Trigon(object):
    """
    Trigon object composed of three points connected by lines.
    """

    def __init__(self, pt1, pt2, pt3):
        self.pt1 = Vuple(pt1)
        self.pt2 = Vuple(pt2)
        self.pt3 = Vuple(pt3)

    @classmethod
    def from_points(cls, pts):
        """

        :param pts:
        :return:
        """
        if len(pts) == 3:
            return Trigon(*pts)
        if len(pts) == 6:
            it = iter(pts)
            return Trigon(*zip(it, it))

    def __str__(self):
        return "<< {}, {}, {} >>".format(self.pt1, self.pt2, self.pt3)

    def __contains__(self, point):
        if type(point) is not Vuple:
            point = Vuple(point)
        return self.area() == sum(map(methodcaller('area'),
                                      self.inner_triangles(point)))

    def inner_triangles(self, point):
        """Triangle funk that returns the three triangles w/ a point

        The point (p) is connected to each point of a triangle. with points,
        a, b, and c. The three triangles are t1=(a, b, p), t2=(a, c, p), and
        t3 = (b, c, p).

        Args:
            point (tuple or Vuple): point to connect to Triangle Vertices

        Returns:
            t1, t2, t3 (Trigon): Three triangles

        """
        t1 = Trigon(point, self.pt2, self.pt3)
        t2 = Trigon(self.pt1, point, self.pt3)
        t3 = Trigon(self.pt1, self.pt2, point)
        return t1, t2, t3

    def is_perimeter_point(self, point):
        """

        Args:
            point:

        Returns:

        """
        if type(point) is not Vuple:
            point = Vuple(point)
        return any(tri_area == 0 for tri_area in
                   map(methodcaller('area'), self.inner_triangles(point)))

    def points(self):
        """

        Returns:

        """
        return self.pt1, self.pt2, self.pt3

    def contains_origin(self):
        """True if the origin (0,0) lies within the Triangle

        Returns:

        """
        return (0, 0) in self

    def area(self):
        """

        Returns:

        """
        return abs(truediv(Vuple.cross(self.pt1 - self.pt2,
                                       self.pt3 - self.pt2), 2))

    @staticmethod
    def area_from_points(pt1, pt2, pt3):
        """

        Args:
            pt1:
            pt2:
            pt3:

        Returns:

        """
        return abs(truediv(Vuple.cross(pt1 - pt2, pt3 - pt2), 2))

class Vuple(tuple):
    """VUPLE == Vector+Tuple"""

    def __new__(cls, *args):
        """

        :param args:
        :return:
        """
        return super(Vuple, cls).__new__(cls, tuple(*args))

    def __gt__(self, other):
        return Vuple.mag_sqrd(self) > Vuple.mag_sqrd(other)

    def __eq__(self, other):
        return all(a == b for a, b in zip(self, other))

    def __add__(self, k):
        if type(k) is int or type(k) is float:
            return Vuple((k + el for el in self))
        elif type(k) is Vuple:
            if len(self) != len(k):
                raise ValueError("Dimensions do NOT match")
            return Vuple(map(add, self, k))

    def __sub__(self, k):
        return Vuple(map(sub, self, k))

    def __mul__(self, k):
        if type(k) is int or type(k) is float:
            return self._mul_scalar(k)

    def __imul__(self, k):
        if type(k) is int or type(k) is float:
            return self._mul_scalar(k)

    def _mul_scalar(self, k):
        return Vuple((k * el for el in self))

    def __truediv__(self, k):
        if type(k) is int or type(k) is float:
            return self._truediv_scalar(k)

    def _truediv_scalar(self, k):
        return Vuple((el / k for el in self))

    def __itruediv__(self, k):
        return self.__truediv__(k)

    def __floordiv__(self, k):
        if type(k) is int or type(k) is float:
            return self._floordiv_scalar_int(k)

    def __ifloordiv__(self, k):
        return self.__floordiv__(k)

    def _floordiv_scalar_int(self, k):
        return Vuple((el // k for el in self))

    def normalize(self):
        """Normalizes the Vuple ST self.magnitude == 1

        :return: Unit Vuple
        """
        return Vuple.unit_vuple(self)

    @staticmethod
    def unit_vuple(voop):
        """

        Args:
            voop:

        Returns:

        """
        return Vuple(voop) / Vuple.mag(voop)

    def get_mag_sqrd(self):
        """

        Returns:

        """
        return Vuple.mag_sqrd(self)

    @staticmethod
    def mag_sqrd(voop):
        """

        Args:
            voop:

        Returns:

        """
        return sum(el * el for el in voop)

    def get_mag(self):
        """

        Returns:

        """
        return Vuple.mag(self)

    @staticmethod
    def mag(voop):
        """

        Args:
            voop:

        Returns:

        """
        return sqrt(Vuple.mag_sqrd(voop))

    @staticmethod
    def dot(a, b):
        """

        Args:
            a:
            b:

        Returns:

        """
        return sum(va * vb for va, vb in zip(a, b))

    @staticmethod
    def cross(v1, v2):
        """Cross product of two 2d vectors

        :param v1: first vector
        :param v2: second vector
        :return: cross product of v1 and v2
        """
        if len(v1) == 2 and len(v2) == 2:
            return (v1[0] * v2[1]) - (v1[1] * v2[0])
        else:
            raise ValueError("cross product gt 2d not implemented")

    @staticmethod
    def angle(v1, v2, radians=False):
        """

        Args:
            v1:
            v2:
            radians:

        Returns:

        """
        # return acos(Vuple.dproduct(v1, v2)/(Vuple.mag(v1)*Vuple.mag(v2)))
        q = 1 if radians else 180 / pi
        return q * acos(Vuple.dot(Vuple.unit_vuple(v1),
                                  Vuple.unit_vuple(v2)))

    def is_disjoint(self, them):
        return len(set(self) & set(them)) == 0

    def product(self):
        """Multiplies all elements in the Vuple

        :return:
        """
        return iter_product(self)
