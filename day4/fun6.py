# funkcje lambda
# skrócony zapis funkcji
# zwraca wynik
# funkcja anonimowa

def odejmij(a, b):
    return a - b


print(odejmij(4, 6))  # -2

odejmij2 = lambda a, b: a - b  # domyślnie ma return
print(odejmij2(5, 7))  # -2

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(11))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(50))  # dorosły

# mapowanie danych
lista = [1, 2, 3, 10, 20, 30, 100, 200, 500]

lista_wyn = []
for i in lista:
    lista_wyn.append(i * 2)
print(lista_wyn)  # [2, 4, 6, 20, 40, 60, 200, 400, 1000]

print([i * 2 for i in lista])  # [2, 4, 6, 20, 40, 60, 200, 400, 1000]


def zmien(x):
    return x * 2


lista_wyn_2 = []
for i in lista:
    lista_wyn_2.append(zmien(i))
print(lista_wyn_2)  # [2, 4, 6, 20, 40, 60, 200, 400, 1000]

# map()  bierze element z kolekcji i wykonuje na nim operacje zadaną funkcją

print(f"Zastosowanie map: {list(map(zmien, lista))}")
# Zastosowanie map: [2, 4, 6, 20, 40, 60, 200, 400, 1000]

# lambda jako funkcja anonimowa, nie posiada nazwy
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie map: {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map: {list(map(lambda x: x * 14, lista))}")
# Zastosowanie map: [2, 4, 6, 20, 40, 60, 200, 400, 1000]
# Zastosowanie map: [4, 8, 12, 40, 80, 120, 400, 800, 2000]
# Zastosowanie map: [14, 28, 42, 140, 280, 420, 1400, 2800, 7000]

# filtrowanie danych
l3 = []
for i in lista:
    if i < 20:
        l3.append(i)
print(l3)  # [1, 2, 3, 10]

# filter() - zwraca elementy spełniające warunek
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 20, lista))}")  # Zastosowanie filter(): [1, 2, 3, 10]
# funkcje wyższego rzedu - filter(), map() - przyjmują inną funkcję jako argument
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 20, lista))}")  # Zastosowanie filter(): [30, 100, 200, 500]
# x > 3 i mniejsze od 100
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3 and x < 100, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 100, lista))}")
# Zastosowanie filter(): [10, 20, 30]
# Zastosowanie filter(): [10, 20, 30]
