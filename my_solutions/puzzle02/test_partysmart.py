import unittest
from partysmart import *

sched1 = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12), (9, 10),
         (10, 11), (10, 12), (11, 12)]
sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
          (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]
sched3 = [(6, 7), (7,9), (10, 11), (10, 12), (8, 10), (9, 11), (6, 8),
          (9, 10), (11, 12), (11, 13), (11, 14)]
sched4 = [(6.0, 8.0, 2), (6.5, 12.0, 1), (6.5, 7.0, 2),
          (7.0, 8.0, 2), (7.5, 10.0, 3), (8.0, 9.0, 2),
          (8.0, 10.0, 1), (9.0, 12.0, 2), (9.5, 10.0, 4),
          (10.0, 11.0, 2), (10.0, 12.0, 3), (11.0, 12.0, 7)]

class TestPartySmart(unittest.TestCase):
    def test_bestTimeToPartySmart(self):
        # Tests using the entire range of the schedule
        self.assertEqual(bestTimeToPartySmart(sched1, 6, 12), 9)
        self.assertEqual(bestTimeToPartySmart(sched2, 6, 12), 9.5)
        self.assertEqual(bestTimeToPartySmart(sched3, 6, 14), 11)
        # Tests using a partial range of the schedule
        self.assertEqual(bestTimeToPartySmart(sched1, 6, 8), 7)
        self.assertEqual(bestTimeToPartySmart(sched2, 6, 8), 7.5)
        self.assertEqual(bestTimeToPartySmart(sched3, 6, 10), 9)
    
    def test_alternativeBestTimeToPartySmart(self):
        self.assertEqual(alternativeBestTimeToPartySmart(sched1), 9)
        self.assertEqual(alternativeBestTimeToPartySmart(sched2), 9.5)
        self.assertEqual(alternativeBestTimeToPartySmart(sched3), 11)
    
    def test_weightedBestTimeToPartySmart(self):
        # Simple test with equal weights; should pick the first interval
        self.assertEqual(weightedBestTimeToPartySmart([[1, 2, 1], [2, 3, 1], [3, 4, 1]]), 1)
        # Simple test with different weights; should pick the interval with the highest-weighted celeb
        self.assertEqual(weightedBestTimeToPartySmart([[1, 2, 1], [2, 3, 2], [3, 4, 3]]), 3)
        self.assertEqual(weightedBestTimeToPartySmart(sched4), 11)