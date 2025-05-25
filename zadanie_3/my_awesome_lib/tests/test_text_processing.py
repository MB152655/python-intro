import unittest
from my_awesome_lib.text_processing import count_words, reverse_text

class TestTextProcessing(unittest.TestCase):
    # Testy dla count_words
    def test_count_words_basic(self):
        self.assertEqual(count_words("Ala ma kota"), 3)

    def test_count_words_empty(self):
        self.assertEqual(count_words(""), 0)

    def test_count_words_multiple_spaces(self):
        self.assertEqual(count_words("Ala   ma   kota"), 3)

    def test_count_words_one_word(self):
        self.assertEqual(count_words("Python"), 1)

    # Testy dla reverse_text
    def test_reverse_text_basic(self):
        self.assertEqual(reverse_text("abc"), "cba")

    def test_reverse_text_empty(self):
        self.assertEqual(reverse_text(""), "")

    def test_reverse_text_palindrome(self):
        self.assertEqual(reverse_text("kajak"), "kajak")

if __name__ == '__main__':
    unittest.main()
