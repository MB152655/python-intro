import unittest
from app import *

class TestEmailValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_emails = [
            "user.name@domain.com",
            "john+doe@sub.domain.co.uk",
            "12345@numbers.org"
        ]
        cls.invalid_emails = [
            "missing@tld",
            "double@@at.com",
            "space in@email.com",
            "user@.com"
        ]

    def test_valid_email_cases(self):
        for i, email in enumerate(self.valid_emails):
            with self.subTest(f"valid_email_{i}"):
                self.assertTrue(is_email_valid(email))

    def test_invalid_email_cases(self):
        for i, email in enumerate(self.invalid_emails):
            with self.subTest(f"invalid_email_{i}"):
                self.assertFalse(is_email_valid(email))

class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ("", True),
            ("a", True),
            ("AbBa", True),
            ("Python", False),
            ("A man, a plan, a canal: Panama", True)
        ]

    def test_palindrome_cases(self):
        for text, expected in self.test_cases:
            with self.subTest(text=text):
                self.assertEqual(is_palindrome(text), expected)

class TestCircleArea(unittest.TestCase):
    def test_valid_radius(self):
        test_cases = [
            (5, 78.5398),
            (0, 0),
            (3.5, 38.4845)
        ]
        for radius, expected in test_cases:
            with self.subTest(radius=radius):
                self.assertAlmostEqual(calculate_circle_area(radius), expected, places=3)

    def test_invalid_inputs(self):
        test_cases = [
            ("string", TypeError),
            (-5, ValueError),
            ([5], TypeError)
        ]
        for input_value, exception in test_cases:
            with self.subTest(input_value=input_value):
                with self.assertRaises(exception):
                    calculate_circle_area(input_value)

class TestFilterEvenNumbers(unittest.TestCase):
    def setUp(self):
        self.valid_inputs = [
            ([1, 2, 3, 4], [2, 4]),
            ([], []),
            ([2, 4, 6], [2, 4, 6])
        ]
        self.invalid_inputs = [
            [1, "2", 3],
            "not a list",
            {'key': 'value'}
        ]

    def test_valid_cases(self):
        for numbers, expected in self.valid_inputs:
            with self.subTest(numbers=numbers):
                self.assertEqual(filter_even_numbers(numbers), expected)

    def test_invalid_cases(self):
        for case in self.invalid_inputs:
            with self.subTest(case=case):
                with self.assertRaises(TypeError):
                    filter_even_numbers(case)

class TestDateFormatConversion(unittest.TestCase):
    def test_valid_dates(self):
        test_cases = [
            ("31/12/2024", "2024-12-31"),
            ("01/01/2023", "2023-01-01"),
            ("28/02/2024", "2024-02-28")
        ]
        for input_date, expected in test_cases:
            with self.subTest(input_date=input_date):
                self.assertEqual(convert_date_format(input_date), expected)

    def test_invalid_dates(self):
        test_cases = [
            ("32/13/2024", ValueError),
            ("2024-12-31", ValueError),
            ("not_a_date", ValueError),
            (12345, TypeError)
        ]
        for input_date, exception in test_cases:
            with self.subTest(input_date=input_date):
                with self.assertRaises(exception):
                    convert_date_format(input_date)

if __name__ == '__main__':
    unittest.main()
