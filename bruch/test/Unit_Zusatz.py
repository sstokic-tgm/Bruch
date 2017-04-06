"""
Created on 27.12.2013

@author: uhs374h
"""
from bruch.Bruch import *
import unittest


class TestAllgemein(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = Bruch(self.b)
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testTuple(self):
        z, n = Bruch(3, 4)
        assert(z == 3 and n == 4)

    def testTuple2(self):
        z, n = self.b
        self.assertEqual(Bruch(z, n), self.b)

    def testTuple3_Error(self):
        b3 = list(self.b2)
        self.assertRaises(IndexError, self.tryIndex, b3, 3)

    @staticmethod
    def tryIndex(obj, index):
        return obj[index]

if __name__ == "__main__":
    unittest.main()