# -*- coding: utf-8 -*-

import unittest
from vector_2d.vector import Vector
from vector_2d.vectorPolar import VectorPolar
import math


def round_vector(vector):
    return vector.__class__(*(round(attribute, 5) for attribute in vector))


class TestVector(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(str(Vector(0, 0)), 'Vector(0, 0)')
        self.assertEqual(str(VectorPolar(0, 0)), 'VectorPolar(0, 0)')

    def test_abs(self):
        self.assertEqual(abs(Vector(0, 0)), 0)
        self.assertEqual(abs(Vector(5, 0)), 5)
        self.assertEqual(abs(Vector(5, 5)), 5 * 2 ** 0.5)
        self.assertEqual(abs(Vector(0, 5)), 5)
        self.assertEqual(abs(Vector(-5, 5)), 5 * 2 ** 0.5)
        self.assertEqual(abs(Vector(-5, 0)), 5)
        self.assertEqual(abs(Vector(-5, -5)), 5 * 2 ** 0.5)
        self.assertEqual(abs(Vector(0, -5)), 5)
        self.assertEqual(abs(Vector(5, -5)), 5 * 2 ** 0.5)

    def test_add(self):
        self.assertEqual(Vector(5, 5) + Vector(2, 1), Vector(7, 6))
        self.assertEqual(Vector(5, 5) + Vector(-2, 1), Vector(3, 6))
        self.assertEqual(Vector(-5, -5) + Vector(-2, -1), Vector(-7, -6))

    def test_sub(self):
        self.assertEqual(Vector(5, 5) - Vector(2, 1), Vector(3, 4))
        self.assertEqual(Vector(5, 5) - Vector(-2, 1), Vector(7, 4))
        self.assertEqual(Vector(-5, -5) - Vector(-2, -1), Vector(-3, -4))

    def test_mul(self):
        self.assertEqual(Vector(3, 5) * 7, Vector(21, 35))

    def test_unit(self):
        self.assertEqual(Vector(1, 0), Vector(6, 0).unit())
        self.assertEqual(Vector(0, 1), Vector(0, 9).unit())
        self.assertEqual(round_vector(Vector(1 / 2 ** 0.5, 1 / 2 ** 0.5)),
                         round_vector(Vector(7, 7).unit()))
        self.assertEqual(round_vector(Vector(-1 / 2 ** 0.5, 1 / 2 ** 0.5)),
                         round_vector(Vector(-8, 8).unit()))

    def test_get_comps(self):
        self.assertEqual(Vector(5, 1).get_comps(), (5, 1))
        self.assertEqual(Vector(5.2, 1.5).get_comps(), (5.2, 1.5))
        self.assertEqual(Vector(5.2, 1.6).get_comps(False), (5, 1))

    def test_set_comp(self):
        vector = Vector(0, 0)
        vector.set_comp(0, 9)
        vector.set_comp(1, 7)
        self.assertEqual(vector, Vector(9, 7))

    def test_neg(self):
        self.assertEqual(-Vector(3, 2), Vector(-3, -2))

    def test_call(self):
        vector = Vector(3, 2)
        self.assertEqual(vector(), (3, 2))
        self.assertEqual(vector(0), 3)
        self.assertEqual(vector(1), 2)

    def test_conversion_to_cartesian(self):
        self.assertEqual(round_vector(VectorPolar(1, 0).to_cartesian()), Vector(1, 0))
        self.assertEqual(round_vector(VectorPolar(1, math.pi / 2.0).to_cartesian()), Vector(0, 1))
        self.assertEqual(round_vector(VectorPolar(1, math.pi).to_cartesian()), Vector(-1, 0))
        self.assertEqual(round_vector(VectorPolar(1, 3 * math.pi / 2.0).to_cartesian()), Vector(0, -1))
        self.assertEqual(round_vector(VectorPolar(1, 2 * math.pi).to_cartesian()), Vector(1, 0))

    def test_iter_cartesian(self):
        tup = (5, 4)
        vector = Vector(*tup)
        for i, attribute in enumerate(vector):
            self.assertEqual(tup[i], attribute)

    def test_iter_polar(self):
        tup = (5, math.pi)
        vector = VectorPolar(*tup)
        for i, attribute in enumerate(vector):
            self.assertEqual(tup[i], attribute)

    def test_conversion_to_polar(self):
        self.assertEqual(round_vector(Vector(1, 0).to_polar()), VectorPolar(1, 0))
        self.assertEqual(Vector(0, 1).to_polar(), VectorPolar(1, math.pi / 2.0))
        self.assertEqual(Vector(0, -1).to_polar(), VectorPolar(1, 3 * math.pi / 2.0))

        vector = Vector(13, 23)
        self.assertEqual(vector, round_vector(vector.to_polar().to_cartesian()))

        vector = VectorPolar(56, 1)
        self.assertEqual(vector, round_vector(vector.to_cartesian().to_polar()))

    def test_int(self):
        self.assertEqual(Vector(3, 5).int(), (3, 5))
        self.assertEqual(Vector(3.2, 5.1).int(), (3, 5))

    def test_div(self):
        self.assertEqual(Vector(5, 5) / 2, Vector(2.5, 2.5))
