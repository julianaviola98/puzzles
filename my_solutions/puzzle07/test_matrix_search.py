import unittest
from matrix_search import *

class TestMatrixSearch(unittest.TestCase):
    t = [[1, 4, 7, 11, 15],
         [2, 5, 8, 12, 19],
         [3, 6, 9, 16, 22],
         [10, 13, 14, 17, 24],
         [18, 21, 23, 26, 30]]
    def test_twoDimensionalBinarySearch(self):
        self.assertEqual(twoDimensionalBinarySearch(7, []), (-1, -1))
        self.assertEqual(twoDimensionalBinarySearch(7, [[]]), (-1, -1))
        self.assertEqual(twoDimensionalBinarySearch(7, [[7]]), (0, 0))
        self.assertEqual(twoDimensionalBinarySearch(7, [[7, 8], [9, 10]]), (0, 0))
        self.assertEqual(twoDimensionalBinarySearch(7, [[6, 7], [8, 9]]), (0, 1))
        self.assertEqual(twoDimensionalBinarySearch(7, [[5, 6], [7, 8]]), (1, 0))
        self.assertEqual(twoDimensionalBinarySearch(7, [[4, 5], [6, 7]]), (1, 1))
        for i in range(len(self.t)):
            for j in range(len(self.t[i])):
                self.assertEqual(twoDimensionalBinarySearch(self.t[i][j], self.t), (i, j))

    def test_altAlgorithm(self):
        self.assertEqual(altAlgorithm(7, []), (-1, -1))
        self.assertEqual(altAlgorithm(7, [[]]), (-1, -1))
        self.assertEqual(altAlgorithm(7, [[7]]), (0, 0))
        self.assertEqual(altAlgorithm(7, [[7, 8], [9, 10]]), (0, 0))
        self.assertEqual(altAlgorithm(7, [[6, 7], [8, 9]]), (0, 1))
        self.assertEqual(altAlgorithm(7, [[5, 6], [7, 8]]), (1, 0))
        self.assertEqual(altAlgorithm(7, [[4, 5], [6, 7]]), (1, 1))
        for i in range(len(self.t)):
            for j in range(len(self.t[i])):
                self.assertEqual(altAlgorithm(self.t[i][j], self.t), (i, j))