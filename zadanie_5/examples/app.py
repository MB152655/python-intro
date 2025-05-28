import numpy as np
import matplotlib.pyplot as plt
import spacy

#NUMPY

# Tworzenie tablic NumPy
tablica_1d = np.array([1, 2, 3, 4, 5])
tablica_2d = np.array([[1, 2, 3], [4, 5, 6]])

print("Tablica 1D:", tablica_1d)
print("Tablica 2D:")
print(tablica_2d)

# Operacje matematyczne na tablicach
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Operacje element po elemencie
suma = a + b
iloczyn = a * b
potega = a ** 2

print("Suma:", suma)
print("Iloczyn:", iloczyn)
print("Potęga:", potega)

# Tworzenie macierzy i operacje
macierz = np.arange(15).reshape(3, 5)
print("\nMacierz 3x5:")
print(macierz)

# Statystyki
print("Suma wszystkich elementów:", macierz.sum())
print("Średnia:", np.mean(macierz))
print("Maksimum w każdym wierszu:", np.max(macierz, axis=1))

# Operacje na macierzach
matrix1 = np.array([[3, 4, 2], [5, 1, 8], [3, 1, 9]])
matrix2 = np.array([[3, 7, 5], [2, 9, 8], [1, 5, 8]])
wynik_mnozenia = np.dot(matrix1, matrix2)
print("\nMnożenie macierzy:")
print(wynik_mnozenia)

#MATPLOTLIB

# Podstawowy wykres liniowy
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 1, 5, 3])

plt.plot(x, y)
plt.title('Podstawowy wykres liniowy')
plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.show()

# Różne typy wykresów
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

# Wykres liniowy z wieloma seriami
x = np.linspace(0, 10, 100)
ax1.plot(x, np.sin(x), label='sin(x)', linewidth=2)
ax1.plot(x, np.cos(x), label='cos(x)', linewidth=2)
ax1.set_title('Funkcje trygonometryczne')
ax1.legend()
ax1.grid(True)

# Wykres punktowy
x_scatter = np.random.randn(50)
y_scatter = np.random.randn(50)
ax2.scatter(x_scatter, y_scatter, alpha=0.6, c='red')
ax2.set_title('Wykres punktowy')

# Histogram
dane = np.random.normal(0, 1, 1000)
ax3.hist(dane, bins=30, alpha=0.7, color='green')
ax3.set_title('Histogram')

# Wykres słupkowy
kategorie = ['A', 'B', 'C', 'D']
wartości = [23, 45, 56, 78]
ax4.bar(kategorie, wartości, color=['blue', 'orange', 'green', 'red'])
ax4.set_title('Wykres słupkowy')

plt.tight_layout()
plt.show()

#SPACY

# Załadowanie modelu językowego dla języka angielskiego
nlp = spacy.load("en_core_web_sm")

# Przetwarzanie tekstu
tekst = "Apple is looking at buying U.K. startup for $1 billion"
doc = nlp(tekst)

# Wyświetlenie tokenów
print("Tokeny:")
for token in doc:
    print(f"{token.text}: {token.pos_}")

# Zaawansowana analiza tekstu
tekst_pl = """
Warszawa jest stolicą Polski. 
Jan Kowalski pracuje jako programista w dużej firmie technologicznej.
Wczoraj spotkał się z Anną Nowak w centrum miasta.
"""

# Dla języka polskiego (jeśli dostępny model)
# nlp_pl = spacy.load("pl_core_news_sm")
# doc_pl = nlp_pl(tekst_pl)

# Przykład z tekstem angielskim
tekst_en = "John Smith works at Google in New York. He met with Sarah Johnson yesterday."
doc_en = nlp(tekst_en)

print("=== ANALIZA TOKENÓW ===")
for token in doc_en:
    print(f"Tekst: {token.text:12} | Lemma: {token.lemma_:10} | POS: {token.pos_:8} | Stop word: {token.is_stop}")

print("\n=== ROZPOZNAWANIE NAZWANYCH JEDNOSTEK ===")
for ent in doc_en.ents:
    print(f"Tekst: {ent.text:15} | Etykieta: {ent.label_:10} | Opis: {spacy.explain(ent.label_)}")

print("\n=== ANALIZA ZALEŻNOŚCI ===")
for token in doc_en:
    if token.dep_ != "punct":
        print(f"{token.text:12} --> {token.head.text:12} ({token.dep_})")

# Segmentacja zdań
print("\n=== SEGMENTACJA ZDAŃ ===")
for i, sent in enumerate(doc_en.sents, 1):
    print(f"Zdanie {i}: {sent.text}")

# Dopasowywanie wzorców
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)

# Wzorzec dla nazw firm
pattern = [{"POS": "PROPN"}, {"LOWER": {"IN": ["inc", "corp", "ltd", "llc"]}}]
matcher.add("COMPANY", [pattern])

matches = matcher(doc_en)
print("\n=== DOPASOWANE WZORCE ===")
for match_id, start, end in matches:
    span = doc_en[start:end]
    print(f"Znaleziono: {span.text}")
