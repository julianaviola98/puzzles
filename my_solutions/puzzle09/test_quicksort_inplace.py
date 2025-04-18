import unittest
from quicksort_inplace import *

class TestQuicksortInPlace(unittest.TestCase):
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    b = [4, 4, 65, 2, -31, 0, 99, 83, -31, 782, 1]
    l = list(range(100))
    d = list(range(99, -1, -1))
    r = [0] * 100
    r[0] = 29
    for i in range(100):
        r[i] = (9679 * r[i-1] + 12637 * i) % 2287

    def test_quicksort(self):
        self.assertEqual(quicksort(self.a, 0, len(self.a) - 1),
                         ([-31, 0, 1, 2, 4, 65, 83, 99, 782], 9, 24))
        self.assertEqual(quicksort(self.b, 0, len(self.b) - 1),
                         ([-31, -31, 0, 1, 2, 4, 4, 65, 83, 99, 782], 13, 29))
        self.assertEqual(quicksort(self.l, 0, len(self.l) - 1),
                         (list(range(100)), 0, 5049))
        self.assertEqual(quicksort(self.d, 0, len(self.d) - 1),
                         (list(range(100)), 50, 5049))
        self.assertEqual(quicksort(self.r, 0, len(self.r) - 1),
                         ([0, 38, 50, 116, 122, 141, 146, 220, 240, 240, 243,
                           275, 288, 305, 306, 306, 307, 387, 419, 431, 433,
                           446, 450, 493, 538, 548, 595, 598, 711, 764, 804,
                           812, 829, 844, 879, 910, 929, 942, 955, 967, 1038,
                           1041, 1049, 1078, 1083, 1102, 1105, 1150, 1153,
                           1154, 1172, 1202, 1208, 1221, 1244, 1266, 1266,
                           1290, 1320, 1384, 1386, 1425, 1428, 1476, 1505,
                           1517, 1520, 1523, 1553, 1582, 1609, 1613, 1625,
                           1639, 1691, 1696, 1725, 1818, 1845, 1884, 1927,
                           1938, 1946, 1949, 1980, 1991, 1995, 2006, 2029,
                           2038, 2047, 2085, 2107, 2115, 2119, 2125, 2188,
                           2215, 2269, 2284],
                          218,
                          683))
        
    def test_quickselect(self):
        c = [4, 65, 2, -31, 0, 99, 83, 782, 1]
        c_sorted = c[:]
        c_sorted.sort()
        for i in range(len(c_sorted)):
            c = [4, 65, 2, -31, 0, 99, 83, 782, 1]
            self.assertEqual(quickselect(c, 0, len(c) - 1, i), c_sorted[i])

        for i in range(100):
            m = list(range(100))
            self.assertEqual(quickselect(m, 0, len(m) - 1, i), m[i])
