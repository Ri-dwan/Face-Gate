import unittest
from palindrome import *

class PalindromeTestCase(unittest.TestCase):

	def test_valid_single_letter(self):
		actual = palindrome("a")
		expected = True
		self.assertEqual(actual, expected)

	def test_valid_empty_string(self):
		actual = palindrome("")
		expected = True
		self.assertEqual(actual, expected)

	def test_valid_word_madam(self):
		actual = palindrome("madam")
		expected = True
		self.assertEqual(actual, expected)

	def test_valid_word_racecar(self):
		actual = palindrome("racecar")
		expected = True
		self.assertEqual(actual, expected)

	def test_valid_word_noon(self):
		actual = palindrome("noon")
		expected = True
		self.assertEqual(actual, expected)

	def test_invalid_word_hello(self):
		actual = palindrome("hello")
		expected = False
		self.assertEqual(actual, expected)

	def test_invalid_word_world(self):
		actual = palindrome("world")
		expected = False
		self.assertEqual(actual, expected)
	
	def test_invalid_word_python(self):
		actual = palindrome("python")
		expected = False
		self.assertEqual(actual, expected)

	def test_invalid_word_ab(self):
		actual = palindrome("ab")
		expected = False
		self.assertEqual(actual, expected)
