import unittest
from reverse import reverse

class ReverseTestCase(unittest.TestCase):

   
    def test_character_at_start(self):
        result = reverse("abcdef")
        expected = "abcdef"  
        self.assertEqual(result, expected)

    def test_character_at_end(self):
        result = reverse("abcdef")
        expected = "abcdef" 
        self.assertEqual(result, expected)


