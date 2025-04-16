import unittest
from tiling import *

class TestTiling(unittest.TestCase):
    def test_tileYardWith4MissingTiles(self):
        self.assertTrue(tileYardWith4MissingTiles(3, [(4, 4), (1, 1), (2, 1), (1, 2)]))
        self.assertTrue(tileYardWith4MissingTiles(3, [(3, 7), (4, 4), (4, 6), (4, 7)]))
        self.assertFalse(tileYardWith4MissingTiles(3, [(4, 4), (3, 1), (2, 1), (1, 2)]))
        self.assertFalse(tileYardWith4MissingTiles(3, [(0, 0), (0, 1), (0, 2), (0, 3)]))