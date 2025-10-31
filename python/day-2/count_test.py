
import unittest
from count import count

class CountTestCase(unittest.TestCase):


    def test_no_count(self):
        result = count("Hello World")
        expected = 0
        self.assertEqual(result, expected)

    def test_multiple_occurrences(self):
        result = count("banana")
        expected = 3
        self.assertEqual(result, expected)

    