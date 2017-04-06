"""
Created on 27.12.2013

@author: uhs374h
"""
import unittest
from bruch.Bruch import *


class TestVergleich(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = Bruch(self.b)
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testEqual(self):
        assert(self.b == self.b2)

    def testNotEqual(self):
        assert(self.b != self.b3)

    def testGE(self):
        assert(self.b >= self.b2)

    def testLE(self):
        assert(self.b <= self.b2)

    def testLT(self):
        assert(self.b < self.b3)

    def testGT(self):
        assert(self.b3 > self.b2)


if __name__ == "__main__":
    unittest.main()