import re
import math
from datetime import datetime
from typing import List

# 1. Walidacja adresu e-mail
def is_email_valid(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    return re.match(pattern, email) is not None

# 2. Sprawdzanie palindromu
def is_palindrome(text: str) -> bool:
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return cleaned == cleaned[::-1]

# 3. Obliczanie pola koła
def calculate_circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Promień nie może być ujemny")
    return math.pi * radius ** 2

# 4. Filtrowanie parzystych liczb
def filter_even_numbers(numbers: List[int]) -> List[int]:
    if not all(isinstance(n, int) for n in numbers):
        raise TypeError("Lista musi zawierać tylko liczby całkowite")
    return [n for n in numbers if n % 2 == 0]

# 5. Konwersja formatu daty
def convert_date_format(date_str: str) -> str:
    try:
        date = datetime.strptime(date_str, "%d/%m/%Y")
        return date.strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError("Nieprawidłowy format daty. Oczekiwano DD/MM/YYYY")
