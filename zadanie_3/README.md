# my_awesome_lib

**my_awesome_lib** to lekka biblioteka narzędziowa w języku Python, która oferuje przydatne funkcje do pracy z danymi, prostych obliczeń matematycznych oraz przetwarzania tekstu. Biblioteka została zaprojektowana z myślą o prostocie, czytelności kodu i łatwości ponownego wykorzystania w różnych projektach.

## Główne możliwości

- **data_utils**: Spłaszczanie list zagnieżdżonych, usuwanie duplikatów z list.
- **math_tools**: Obliczanie silni, sprawdzanie czy liczba jest pierwsza.
- **text_processing**: Zliczanie słów w tekście, odwracanie tekstu.

## Instalacja

### Ręczna instalacja (zalecana podczas rozwoju)

git clone https://github.com/MB152655/my_awesome_lib.git
cd my_awesome_lib
pip install -e .

text

### Bezpośrednie użycie w projekcie

Możesz również po prostu skopiować folder `my_awesome_lib` do swojego projektu i zaimportować moduły.

## Przykłady użycia

from my_awesome_lib.data_utils import flatten_list, remove_duplicates
from my_awesome_lib.math_tools import factorial, is_prime
from my_awesome_lib.text_processing import count_words, reverse_text

Operacje na listach
print(flatten_list([, [3, # Wynik: [1,int(remove_duplicates([1, 2, 2, 3,ik: (kolejność może być różna)

Narzędzia matematyczne
print(factorial(5)) # Wynik: 120
print(is_prime(13)) # Wynik: True

Przetwarzanie tekstu
print(count_words("Ala ma kota")) # Wynik: 3
print(reverse_text("Python")) # Wynik: nohtyP

text

## Licencja

MIT License

## Autor

Jan Kowalski

## Wersja

0.1.0
