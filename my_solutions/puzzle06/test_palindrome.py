import unittest
from palindrome import *

class TestPalindrome(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertTrue(isPalindrome(''))
        self.assertTrue(isPalindrome('aa'))
        self.assertTrue(isPalindrome('aba'))
        self.assertTrue(isPalindrome('kayak'))
        self.assertTrue(isPalindrome('kayaK'))
        self.assertTrue(isPalindrome('racecar'))
        self.assertFalse(isPalindrome('Juliana'))
        self.assertFalse(isPalindrome('Viola'))