import unittest
from translator import english_to_french
from translator import french_to_english

class TesteToF(unittest.TestCase):
    """Testing English to French translation"""
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french("None"), '')

class TestfToE(unittest.TestCase):
    """Testing French to English translation"""
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english("None"), '')

unittest.main()
