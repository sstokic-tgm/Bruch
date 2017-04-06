"""
Created on 27.12.2013

@author: uhs374h
"""
import unittest
from bruch.Bruch import *


class TestDivision(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = Bruch(self.b)
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testdiv(self):
        self.b = self.b / Bruch(4)
        assert(float(self.b) == 0.375)

    def testdiv2(self):
        self.b = self.b / self.b3
        assert(float(self.b) == 0.75)

    def testdiv3(self):
        self.b2 = self.b / 2
        assert(float(self.b2) == 0.75)

    def testrdivError(self):
        self.assertRaises(TypeError, self.b2.__rtruediv__, 3.0)

    def testrdiv(self):
        self.b2 = 2 / Bruch(2)
        assert(float(self.b2) == 1)

    def testdivZeroError(self):
        self.assertRaises(ZeroDivisionError, self.b2.__truediv__, 0)

    def testdivTypeError(self):
        self.assertRaises(TypeError, self.b2.__truediv__, 3.1)

    def testdivZeroError2(self):
        self.assertRaises(ZeroDivisionError, self.b2.__truediv__, Bruch(0, 3))

    def testrdivZeroError(self):
        bneu = Bruch(0, 3)
        self.assertRaises(ZeroDivisionError, bneu.__rtruediv__, 3)
        
    def testiDiv(self):
        self.b /= 2
        assert(self.b == Bruch(3, 4))
    
    def testiDiv2(self):
        self.b /= Bruch(2)
        assert(self.b == Bruch(3, 4))

    def testiDivError(self):
        self.assertRaises(TypeError, self.b.__itruediv__, "other")

if __name__ == "__main__":
    unittest.main()