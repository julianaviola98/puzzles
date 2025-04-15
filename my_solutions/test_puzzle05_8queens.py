import unittest
from puzzle05_8queens import *

class TestPuzzle05_8Queens(unittest.TestCase):
    def test_EightQueens(self):
        self.assertEqual(EightQueens(1, [-1] * 8), [[0, 4, 7, 5, 2, 6, 1, 3]])
        self.assertEqual(EightQueens(2, [-1] * 8), [[0, 4, 7, 5, 2, 6, 1, 3],
                                                    [0, 5, 7, 2, 6, 3, 1, 4]])
        self.assertEqual(EightQueens(4, [-1] * 8), [[0, 4, 7, 5, 2, 6, 1, 3],
                                                    [0, 5, 7, 2, 6, 3, 1, 4],
                                                    [0, 6, 3, 5, 7, 1, 4, 2],
                                                    [0, 6, 4, 7, 1, 3, 5, 2]])
        self.assertEqual(EightQueens(8, [-1] * 8), [[0, 4, 7, 5, 2, 6, 1, 3],
                                                    [0, 5, 7, 2, 6, 3, 1, 4],
                                                    [0, 6, 3, 5, 7, 1, 4, 2],
                                                    [0, 6, 4, 7, 1, 3, 5, 2],
                                                    [1, 3, 5, 7, 2, 0, 6, 4],
                                                    [1, 4, 6, 0, 2, 7, 5, 3],
                                                    [1, 4, 6, 3, 0, 7, 5, 2],
                                                    [1, 5, 0, 6, 3, 7, 2, 4]])
        self.assertEqual(EightQueens(1, [-1, 4, -1, -1, -1, -1, -1, 0]), [[2, 4, 1, 7, 5, 3, 6, 0]])