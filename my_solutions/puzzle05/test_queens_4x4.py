import unittest
from queens_4x4 import *

class TestQueens_4x4(unittest.TestCase):
    def test_FourQueens(self):
        self.assertEqual(FourQueens(), [[[0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]],
                                        [[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]]])