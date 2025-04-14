import sys
import unittest
from io import StringIO
from puzzle03 import *

class TestPuzzle03(unittest.TestCase):
    def test_ComputerAssistant(self):
        self.assertTrue(ComputerAssistant(100000, '6_H'))
        self.assertTrue(ComputerAssistant(200000, '5_C'))
        self.assertTrue(ComputerAssistant(300000, '7_H'))
        self.assertTrue(ComputerAssistant(400000, '9_C'))
        self.assertTrue(ComputerAssistant(500000, '7_C'))

    def test_choosePairSuit(self):
        # If there's only one suit, should choose that suit
        self.assertEqual(choosePairSuit([0], [0, 0, 1, 2, 3], [0, 1, 0, 1, 2]), 0)
        # If there are two suits, each with the same two cards, choose the second suit
        self.assertEqual(choosePairSuit([0, 1], [0, 0, 1, 1, 2], [0, 1, 0, 1, 0]), 1)
        # If there are two suits, and the distance between each same-pair suit is n, choose the second suit
        self.assertEqual(choosePairSuit([0, 1], [0, 0, 1, 1, 2], [0, 1, 2, 3, 0]), 1)
        # If there are two suits, choose the suit with the minimum distance for one of its pairs
        # In this case, 7-0 > 3-2, so choose the second suit
        self.assertEqual(choosePairSuit([0, 1], [0, 0, 1, 1, 2], [0, 7, 2, 3, 0]), 1)
        # In this case, 3-2 < 7-0, so choose the first suit
        self.assertEqual(choosePairSuit([0, 1], [0, 0, 1, 1, 2], [2, 3, 0, 7, 0]), 0)
        # Take into account all possible pairs in a given suit
        self.assertEqual(choosePairSuit([0, 1], [0, 0, 1, 1, 1], [0, 4, 0, 3, 7]), 1)
        # Test that the distance between K (12) and A (0) is 1
        self.assertEqual(choosePairSuit([0, 1], [0, 0, 1, 1, 2], [12, 0, 2, 4, 0]), 0)

    def test_outputNext3Cards(self):
        # Same suit
        self.assertEqual(outputNext3Cards(1, [0, 1, 2]), ['A_C', '2_C', '3_C'])
        self.assertEqual(outputNext3Cards(2, [0, 1, 2]), ['A_C', '3_C', '2_C'])
        self.assertEqual(outputNext3Cards(3, [0, 1, 2]), ['2_C', 'A_C', '3_C'])
        self.assertEqual(outputNext3Cards(4, [0, 1, 2]), ['2_C', '3_C', 'A_C'])
        self.assertEqual(outputNext3Cards(5, [0, 1, 2]), ['3_C', 'A_C', '2_C'])
        self.assertEqual(outputNext3Cards(6, [0, 1, 2]), ['3_C', '2_C', 'A_C'])
        # Same value but different suits
        self.assertEqual(outputNext3Cards(1, [0, 1, 2]), ['A_C', 'A_D', 'A_H'])
        self.assertEqual(outputNext3Cards(2, [0, 1, 2]), ['A_C', 'A_H', 'A_D'])
        self.assertEqual(outputNext3Cards(3, [0, 1, 2]), ['A_D', 'A_C', 'A_H'])
        self.assertEqual(outputNext3Cards(4, [0, 1, 2]), ['A_D', 'A_H', 'A_C'])
        self.assertEqual(outputNext3Cards(5, [0, 1, 2]), ['A_H', 'A_C', 'A_D'])
        self.assertEqual(outputNext3Cards(6, [0, 1, 2]), ['A_H', 'A_D', 'A_C'])
