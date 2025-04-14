import unittest
from puzzle04 import *

class TestPuzzle04(unittest.TestCase):
    def test_determineRadixAndNumBalls(self):
        self.assertEqual(determineRadixAndNumBalls(128, 6), (3, 5))

    def test_howHardIsTheCrystal(self):
        self.assertEqual(howHardIsTheCrystal(128, 2, ['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
                                                      'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
                                                      'no', 'yes']),
                         (1, [[1, 128], [13, 128], [25, 128], [37, 128], [49, 128], [61, 128],
                              [73, 128], [85, 128], [97, 128], [109, 128], [121, 128], [122, 128],
                              [123, 128], [124, 128], [125, 128], [126, 128], [127, 128], [128, 128]]))
        self.assertEqual(howHardIsTheCrystal(128, 2, ['no', 'yes', 'no', 'yes']),
                         (2, [[1, 128], [13, 128], [13, 23], [14, 23]]))
        self.assertEqual(howHardIsTheCrystal(128, 3, ['no', 'yes', 'no', 'yes', 'no', 'yes']),
                         (3, [[1, 128], [37, 128], [37, 71], [43, 71], [43, 47], [44, 47]]))