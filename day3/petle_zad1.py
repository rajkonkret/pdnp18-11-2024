# pętle - możliwość wykonania wieokrotnie tego samego fragmentu programu
# for - pętla iteracyjna
import random

from day1.teksty import encode_s

for i in range(5):  # od 0 do 4
    print(i)
# 0
# 1
# 2
# 3
# 4

for i in range(10000):
    pass  # nic nie rób

for _ in range(5):  # _ - niema zmienna
    print('to jest pętla')
    # print(_)
# to jest pętla
# to jest pętla
# to jest pętla
# to jest pętla
# to jest pętla

for i in range(20):  # od 0 do 19
    print(i * 2)  # 38

print("------")
"""Return random integer in range [a, b], including both end points."""
print(random.randint(1, 100))  # 21, int od 1 do 100 włącznie
print(random.randrange(1, 100))  # int od 1 do 99, 36
print(random.randrange(5))  # int od 0 do 4, 1
print(random.random())  # float 0.25115282757340995, pd 0 do 0.999999
print(random.random() * 5)  # float 2.804473691311862, pd 0 do 4.999999

lista = [67, 45, 32, 68, 89, 90, 42]
print(random.choice(lista))  # 89

print("----lotto----")
lista_kule = list(range(1, 50))  # od 1 do 49
# print(lista_kule)

lista_wylosowane = []
for _ in range(6):  # od 0 do 5 czyli 6 razy
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)  # usunięcie elementu z listy
    lista_wylosowane.append(wyn)

print(lista_wylosowane)  # [16, 22, 26, 34, 32, 2]

print(random.choices(lista_kule, k=6))  # [39, 5, 44, 44, 7, 33], losowanie z powtórzeniami
print(random.sample(lista_kule, k=6))  # [29, 17, 2, 34, 1, 45], losowanie bez powtórzeń
print(random.sample(lista_kule, 6))  # [48, 15, 18, 36, 42, 46]

for i in range(10):  # od 0 do 9
    if i % 2 == 0:  # % - modulo, "reszta" z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# list comprehension
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista_wylosowane:
    if c > 10:
        print("Większe od 10")
    elif c == 10:
        print("Równe")
    else:
        print("Mniejsze")
# Większe od 10
# Większe od 10
# Większe od 10
# Większe od 10
# Większe od 10
# Mniejsze

for i in range(0, 10, 2):  # (start, stop,krok)
    print(i)
# 0
# 2
# 4
# 6
# 8

for i in range(10, 0, -2):  # krok ujemny, czyli w dół
    print(i)
# 10
# 8
# 6
# 4
# 2

for i in range(-5, 0):
    print(i)
# -5
# -4
# -3
# -2
# -1

for c in lista3:
    if c == 2:
        c += 1
        print("Tylko gdy c=2", c)
    print("Przy każdym elemencie pętli", c)
# Przy każdym elemencie pętli 0
# Tylko gdy c=2 3
# Przy każdym elemencie pętli 3
# Przy każdym elemencie pętli 4
# Przy każdym elemencie pętli 6
# Przy każdym elemencie pętli 8

imiona = ['Radek', 'Tomek', "Zenek", "Ania"]
print(type(imiona))
print(imiona)
# <class 'list'>
# ['Radek', 'Tomek', 'Zenek', 'Ania']

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Ania

# 0 Radek

for i in range(len(imiona)):  # range(4) od 0 do 3
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for i in imiona:
    print(imiona.index(i), i)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate() - zwraca elemnt i pozycję na której się znajduje
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Ania')
a, b = (3, 'Ania')
print(a, b)  # 3 Ania
for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania
for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

imiona = ['Radek', 'Tomek', "Zenek", "Ania"]
wiek = [44, 55, 65, 24]

# wypisać Radek 44
for i in imiona:
    print(i, wiek[imiona.index(i)])
# Radek 44
# Tomek 55
# Zenek 65
# Ania 24
imiona = ['Radek', 'Tomek', "Zenek", "Ania", "Joanna"]
wiek = [44, 55, 65, 24]

# wypisać Radek 44
# for i in imiona:
#     print(i, wiek[imiona.index(i)]) # IndexError: list index out of range
# zip() - połącz kolekcje
for i in zip(imiona, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 65)
# ('Ania', 24)
for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 44
# Tomek 55
# Zenek 65
# Ania 24

# 0 Radek 44
for i in enumerate(zip(imiona, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Tomek', 55))
# (2, ('Zenek', 65))
# (3, ('Ania', 24))
a, b = (0, ('Radek', 44))
print(a, b)  # 0 ('Radek', 44)
c, d = ('Radek', 44)
print(c, d) # Radek 44
(a, (c, d)) = (0, ('Radek', 44))
print(f"{a=} {c=} {d=}")  # a=0 c='Radek' d=44

for i, (imie, w) in enumerate(zip(imiona, wiek)):
    print(i, imie, w)
# 0 Radek 44
# 1 Tomek 55
# 2 Zenek 65
# 3 Ania 24
