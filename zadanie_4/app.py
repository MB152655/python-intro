import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm.helpers import rrankdata

# 1. DANE
print("1. Przygotowanie danych")
print("-" * 30)

# Macierz decyzyjna (5 alternatyw, 3 kryteria)
matrix = np.array([
    [100, 8.0, 150],  # Alt A
    [80,  7.0, 120],  # Alt B  
    [120, 9.0, 180],  # Alt C
    [70,  6.5, 100],  # Alt D
    [90,  7.5, 140]   # Alt E
])

alternatives = ['A', 'B', 'C', 'D', 'E']
criteria = ['Cena', 'Spalanie', 'Moc']

# Typy: -1=min, 1=max
types = np.array([-1, -1, 1])  # Cena(min), Spalanie(min), Moc(max)

# Wagi (suma=1)
weights = np.array([0.4, 0.3, 0.3])

print("Dane:")
df = pd.DataFrame(matrix, index=alternatives, columns=criteria)
print(df)
print(f"Typy: {types}")
print(f"Wagi: {weights}")

# 2. TOPSIS
print("\n2. TOPSIS")
print("-" * 30)

topsis = TOPSIS()
topsis_scores = topsis(matrix, weights, types)
topsis_ranking = rrankdata(topsis_scores)

print(f"Wyniki: {topsis_scores.round(3)}")
print(f"Ranking: {topsis_ranking}")

# 3. SPOTIS
print("\n3. SPOTIS")
print("-" * 30)

bounds = np.array([
    [matrix[:, 0].min(), matrix[:, 0].max()],  # Cena
    [matrix[:, 1].min(), matrix[:, 1].max()],  # Spalanie
    [matrix[:, 2].min(), matrix[:, 2].max()]   # Moc
])

spotis = SPOTIS(bounds)
spotis_scores = spotis(matrix, weights, types)

spotis_ranking = rrankdata(spotis_scores)

print(f"Wyniki: {spotis_scores.round(3)}")
print(f"Ranking: {spotis_ranking}")

# 4. PORÓWNANIE
print("\n Porównanie")

results = pd.DataFrame({
    'Alt': alternatives,
    'TOPSIS': topsis_ranking,
    'SPOTIS': spotis_ranking
})

print(results)

# Najlepsze alternatywy
best_topsis = alternatives[np.argmin(topsis_ranking)]
best_spotis = alternatives[np.argmin(spotis_ranking)]

print(f"\nNajlepsza TOPSIS: {best_topsis}")
print(f"Najlepsza SPOTIS: {best_spotis}")

if best_topsis == best_spotis:
    print("Obie metody wskazują tę samą alternatywę!")
else:
    print("Metody wskazują różne alternatywy")

