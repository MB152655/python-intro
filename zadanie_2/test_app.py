import unittest
import app

class TestEmailValidation(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(app.is_email_valid("user@example.com"))

    def test_invalid_email_no_at(self):
        self.assertFalse(app.is_email_valid("userexample.com"))

    def test_invalid_email_multiple_ats(self):
        self.assertFalse(app.is_email_valid("user@@example.com"))
