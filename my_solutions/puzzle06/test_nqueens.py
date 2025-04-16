import unittest
from nqueens import *

class TestNQueens(unittest.TestCase):
    def test_printSolution(self):
        self.assertEqual(printSolution([1, 3, 0, 2]),
                         ('. . Q .\n'
                          'Q . . .\n'
                          '. . . Q\n'
                          '. Q . .'))
        self.assertEqual(printSolution([0, 4, 7, 5, 2, 6, 1, 3]),
                         ('Q . . . . . . .\n'
                          '. . . . . . Q .\n'
                          '. . . . Q . . .\n'
                          '. . . . . . . Q\n'
                          '. Q . . . . . .\n'
                          '. . . Q . . . .\n'
                          '. . . . . Q . .\n'
                          '. . Q . . . . .'))
        
    def test_nQueens(self):
        self.assertEqual(nQueens(4, [2, 0, 3, 1]),
                         ('. Q . .\n'
                          '. . . Q\n'
                          'Q . . .\n'
                          '. . Q .'))
        self.assertEqual(nQueens(8, [7, -1, -1, -1, -1, -1, -1, -1]),
                         ('. . . Q . . . .\n'
                          '. Q . . . . . .\n'
                          '. . . . . . Q .\n'
                          '. . Q . . . . .\n'
                          '. . . . . Q . .\n'
                          '. . . . . . . Q\n'
                          '. . . . Q . . .\n'
                          'Q . . . . . . .'))
        self.assertEqual(nQueens(10, [-1, -1, 4, -1, -1, -1, -1, 0, -1, 5]),
                         ('. . . . . . . Q . .\n'
                          '. . . . Q . . . . .\n'
                          '. Q . . . . . . . .\n'
                          '. . . . . . . . Q .\n'
                          '. . Q . . . . . . .\n'
                          '. . . . . . . . . Q\n'
                          '. . . . . . Q . . .\n'
                          '. . . Q . . . . . .\n'
                          '. . . . . Q . . . .\n'
                          'Q . . . . . . . . .'))