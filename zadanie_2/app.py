import re

#sprawdzenie poprawosci adresu e-mail
def is_email_valid(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


#obliczanie pola koła
class TestCircleArea(unittest.TestCase):
    def test_valid_radius(self):
        self.assertAlmostEqual(app.calculate_circle_area(3), 28.2743, places=4)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            app.calculate_circle_area(-1)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            app.calculate_circle_area("abc")



#
import math

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2
