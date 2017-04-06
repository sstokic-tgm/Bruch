"""
Created on 27.12.2013

@author: uhs374h
"""
import unittest
from bruch.Bruch import *


class TestSubtraktion(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = Bruch(self.b)
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testminus(self):
        self.b = self.b - Bruch(4, 5)
        assert(float(self.b) == 0.7)

    def testminus2(self):
        self.b = self.b - self.b3
        assert(float(self.b) == -0.5)

    def testminus3(self):
        self.b2 = self.b - Bruch(1)
        assert(float(self.b2) == 0.5)

    def testiSubError(self):
        self.assertRaises(TypeError, self.b.__isub__, "other")

    def testrsubError(self):
        """TypeError!!!

        self.b2=2.0-self.b2
        """
        self.assertRaises(TypeError, self.b2.__rsub__, 2.0)

    def testiSub(self):
        self.b -= 2
        assert(self.b == Bruch(-1, 2))

    def testiSub2(self):
        self.b -= Bruch(2)
        assert(self.b == Bruch(-1, 2))

    def testrsub(self):
        self.b2 = 3 - Bruch(3, 2)
        assert(float(self.b2) == 1.5)


if __name__ == "__main__":
    unittest.main()