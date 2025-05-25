# 1. Walidacja e-mail
import re
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

# 2. Obliczanie pola koła
import math
def circle_area(radius):
    if radius < 0:
        raise ValueError("Promień nie może być ujemny")
    return math.pi * radius ** 2

# 3. Filtrowanie listy
def filter_even(numbers):
    return [num for num in numbers if num % 2 == 0]

# 4. Konwersja daty
from datetime import datetime
def convert_date(date_str):
    try:
        date = datetime.strptime(date_str, "%d/%m/%Y")
        return date.strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError("Nieprawidłowy format daty")

# 5. Sprawdzanie palindromu
def is_palindrome(text):
    cleaned = ''.join(filter(str.isalnum, text.lower()))
    return cleaned == cleaned[::-1]
