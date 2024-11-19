# zbiór - set - przechowuje unikalne wartości
# nie zachowuje kolejności przy dodawaniu
# nie ma indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # set() - zamiana na zbiór
print(type(zbior))  # <class 'set'>
print(zbior)  # {33, 66, 777, 11, 44, 22, 55} straciliśmy kolejność

# utworzenie pustego zbioru
zb2 = set()
print(zb2)  # set() - pusty zbiór
print(type(zb2))  # <class 'set'>

# dodanie elementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(24)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 24}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24}

# pop() usunięcie pierwszego eleementu
print(zbior.pop())  # 33 - pierwszy element

zbior_copy = zbior.copy()
print(zbior)
print(zbior_copy)
print(id(zbior))
print(id(zbior_copy))
# {66, 777, 11, 44, 18, 22, 24}
# {66, 18, 22, 24, 777, 11, 44}
# 2943989571744
# 2943989567264

zbior_2 = {667, 11, 44, 18, 52, 62, 999, 999, 12.34}
print(type(zbior_2))  # <class 'set'>
print(zbior_2)  # {999, 11, 44, 12.34, 18, 52, 667, 62}

# suma zbiorów - dostajemy nowy zbió
print(zbior | zbior_2)  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}
print(zbior.union(zbior_2))  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}

# częśc wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica
print(zbior - zbior_2)  # {24, 777, 66, 22}
print(zbior.difference(zbior_2))  # {24, 777, 66, 22}
# {66, 777, 11, 44, 18, 22, 24} - {999, 11, 44, 12.34, 18, 52, 667, 62} ={66, 777, 22, 24}

# łaczy zbiory, zmienia bazowy !!!
zbior.update(zbior_2)
print(zbior)  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}, zmiana zawartosci zbior

lista = list(zbior_2)
print(lista)
print(type(lista))
# [999, 11, 44, 12.34, 18, 52, 667, 62]
# <class 'list'>

print(999 in zbior)  # True

# sortowanie zbioru zwróci liste
print(sorted(zbior))  # [11, 12.34, 18, 22, 24, 44, 52, 62, 66, 667, 777, 999]
print(zbior)  # zbiór zostanie niezmieniony, nie ma indeksu, {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}
