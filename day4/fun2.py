# funkcje zwracające wynik
# konczy sie słówkiem return
# gdy napotka n return kończy działnie w funkcji


def dodaj(a, b):
    return a + b


def odejmij(a, b=0, c=0):
    return a - b - c


dodaj(57, 45)
print(dodaj(57, 45))  # 102
wynik = dodaj(45, 78)
print("Wynik", wynik)  # Wynik 123

print(odejmij(1))
print(odejmij(1, 2))
print(odejmij(1, 2, 3))
# 1
# -1
# -4

print(odejmij(b=9, a=10))
print(odejmij(b=9, a=10, c=89))
# 1
# -88

print(odejmij(1, c=89))  # -88
print(odejmij(1, c=89, b=78))  # -166

print(dodaj(4, 5) + odejmij(1, 2, 3))  # 5
