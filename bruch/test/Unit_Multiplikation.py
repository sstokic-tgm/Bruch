"""
Created on 27.12.2013

@author: uhs374h
"""
import unittest
from bruch.Bruch import *


class TestMultiplikation(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = Bruch(self.b)
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testmal(self):
        self.b = self.b * Bruch(4)
        assert(float(self.b) == 6)

    def testmal2(self):
        self.b = self.b * self.b2
        assert(float(self.b) == 2.25)

    def testmal3(self):
        self.b2 = self.b * 2
        assert(float(self.b2) == 3)

    def testiMulError(self):
        self.assertRaises(TypeError, self.b.__imul__, "other")

    def testiMul(self):
        self.b *= 2
        assert(self.b == 3)

    def testiMul2(self):
        self.b *= Bruch(2)
        assert(self.b == 3)

    def testrmal(self):
        self.b2 = 2 * Bruch(3, 2)
        assert(float(self.b2) == 3)

    def testmulError(self):
        self.assertRaises(TypeError, self.b2.__mul__, 2.0)

if __name__ == "__main__":
    unittest.main()