# my_awesome_lib/math_tools.py
def factorial(n):
    """Oblicza silnię liczby całkowitej n."""
    if n < 0:
        raise ValueError("n musi być nieujemne")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def is_prime(n):
    """Sprawdza, czy liczba jest pierwsza."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
