import random  # Moduł do operacji losowych https://docs.python.org/3/library/random.html

# Tworzenie dwóch list
list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3, 4]

# Łączenie list funkcją zip() https://docs.python.org/3/library/functions.html#zip
zipped_list = list(zip(list1, list2))
print("Połączone listy:", zipped_list)

# Wybór losowego elementu z połączonej listy (random.choice) https://docs.python.org/3/library/random.html#random.choice
random_element = random.choice(zipped_list)
print("Losowy element z połączonej listy:", random_element)

# Obsługa wyjątku try-except https://docs.python.org/3/library/exceptions.html#ValueError
try:
    user_input = input("Podaj liczbę: ")
    number = int(user_input)  # Próba konwersji inputu na liczbę całkowitą
    print("Podana liczba to:", number)
except ValueError as e:
    print("Błąd: Podana wartość nie jest liczbą całkowitą!", e)
