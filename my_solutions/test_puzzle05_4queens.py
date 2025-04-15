import unittest
from puzzle05_4queens import *

class TestPuzzle05_4Queens(unittest.TestCase):
    def test_FourQueens(self):
        self.assertEqual(FourQueens(), [[[0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]],
                                        [[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]]])