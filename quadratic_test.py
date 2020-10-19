from quadratic import split_middle_term
import unittest

class TestSplitMiddleTerm(unittest.TestCase):
    def test_basic(self):
        a, b, c = 1, 6, 8 # TestCase
        expected = 2, 4
        self.assertEqual(split_middle_term(a, b, c), expected)

    def test_one(self):
        a, b, c = 3, 5, 2
        expected = 2, 3
        self.assertEqual(split_middle_term(a, b, c), expected)


unittest.main()
