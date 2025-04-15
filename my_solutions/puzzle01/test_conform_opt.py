import unittest
from conform_opt import *

caps1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F' ]
caps2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F' ]
caps3 = ['F', 'F', 'B', 'H', 'B', 'F', 'B', 'B', 'B', 'F', 'H', 'F', 'F']

class TestConformOpt(unittest.TestCase):
    def test_pleaseConformOpt(self):
        self.assertEqual(pleaseConformOpt([]), [])
        self.assertEqual(pleaseConformOpt(['F']), [])
        self.assertEqual(pleaseConformOpt(['B']), [])
        self.assertEqual(pleaseConformOpt(['F', 'B']), [[1, 1]])
        self.assertEqual(pleaseConformOpt(caps1), [[2, 4], [6, 8], [11, 11]])
        self.assertEqual(pleaseConformOpt(caps2), [[2, 4], [6, 8]])
        self.assertEqual(pleaseConformOpt(caps3), [[2, 2], [4, 4], [6, 8]])

    def test_pleaseConformOnepass(self):
        self.assertEqual(pleaseConformOnepass([]), [])
        self.assertEqual(pleaseConformOnepass(['F']), [])
        self.assertEqual(pleaseConformOnepass(['B']), [])
        self.assertEqual(pleaseConformOnepass(['F', 'B']), [[1, 1]])
        self.assertEqual(pleaseConformOnepass(caps1), [[2, 4], [6, 8], [11, 11]])
        self.assertEqual(pleaseConformOnepass(caps2), [[2, 4], [6, 8]])
        # pleaseConformOnepass doesn't handle hatless people (caps3)
