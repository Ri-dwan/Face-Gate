import unittest
from sum import sum

class SumTestCase(unittest.TestCase):

	def test_example_case(self):
		result = sum([1, 2, 3, 2])
		expected = 4  
		self.assertEqual(result, expected)

	def test_all_duplicates(self):
		result = sum([11111])
		expected = 0
		self.assertEqual(result, expected)
	
	def test_all_unique(self):
		result = sum([1, 2, 3])
		expected = 6 
		self.assertEqual(result, expected)

	def test_empty(self):
		result = sum([])
		expected = 0
		self.assertEqual(result, expected)