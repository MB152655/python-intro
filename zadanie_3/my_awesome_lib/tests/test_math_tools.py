import unittest
from my_awesome_lib.math_tools import factorial, is_prime

class TestMathTools(unittest.TestCase):
    # Testy dla factorial
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(1), 1)

    def test_factorial_large(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-3)

    # Testy dla is_prime
    def test_is_prime_true(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(13))

    def test_is_prime_false(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(25))

    def test_is_prime_negative(self):
        self.assertFalse(is_prime(-7))

if __name__ == '__main__':
    unittest.main()
