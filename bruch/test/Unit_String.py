"""
Created on 27.12.2013

@author: uhs374h
"""
import unittest
from bruch.Bruch import *


class TestString(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = Bruch(self.b)
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def teststr(self):
        str1 = "(3/2)"
        assert(str(self.b) == str1)

    def teststr2(self):
        b2 = Bruch(-3, -2)
        str1 = "(3/2)"
        assert(str(b2) == str1)


if __name__ == "__main__":
    unittest.main()