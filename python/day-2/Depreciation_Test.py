import unittest
from Depreciation import depreciation

class DepreciationTestCase(unittest.TestCase):

    def test_depreciation_1_year(self):
 
        actual = depreciation(50000, years=1, rate=0.08)
        expected = 4000
        self.assertEqual(actual, expected)

    def test_depreciation_3_years(self):
        actual = depreciation(50000, years=3, rate=0.08)
        expected = 1333.33 
        self.assertAlmostEqual(actual, expected, places=2)

    def test_depreciation_2_rate(self):
        actual = depreciation(50000, years=1, rate=0.04)
        expected = 2000
        self.assertEqual(actual, expected)