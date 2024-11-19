# krotka, tuple - kolekcja, przechowuje dowolną ilość elementów
# kolekcja niemutowalna, do odczytu
# pozwala lepiej zarzadzac pamięcią
# krotka jednolementowa - stała - zmienna

tupla = "Radek"
print(type(tupla))  # str

tupla1 = ("Radek")
print(tupla1)
print(type(tupla1))  # <class 'str'>

tupla2 = "Radek",
print(tupla2)
print(type(tupla2))  # <class 'tuple'>

# PEP8 zaleca by tuple jednoelementowa tworzyc z nawiasami
tupla3 = ("Radek",)
print(type(tupla3))  # <class 'tuple'>

tupla_liczby = 43, 55, 22.34, 11, 200
print(type(tupla_liczby))
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

# tupla jest niemutowalna
# tupla_liczby[2] = 123 # TypeError: 'tuple' object does not support item assignment

tupla_imiona = "Radek", "Tomek", 'Zenek', 'Marcin', "Ania", "Zosia"
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Marcin', 'Ania', 'Zosia')
print(type(tupla_liczby))  # <class 'tuple'>

print(tupla_imiona.index("Radek"))  # indeks numer 0
print(tupla_imiona.count("Zenek"))  # występuje 1 raz

print(len(tupla_imiona))  # długość 6

# sorted() - sortowanie kolekcji, zwraca listę z posortowanymi elementami
print(sorted(tupla_imiona))  # ['Ania', 'Marcin', 'Radek', 'Tomek', 'Zenek', 'Zosia']
# nie zmieni krotki
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Marcin', 'Ania', 'Zosia')

# rozpakowanie tupli
tup = 1, 2
print(type(tup))  # <class 'tuple'>
a, b = 1, 2
print(a, b)  # 1 2
a, b = tup
print(a, b)  # 1 2
tup2 = 1, 2, 3
# a, b = tup2  # ValueError: too many values to unpack (expected 2)
a, *b = tup2  # * worek na dane
print(a, b)  # 1 [2, 3]

print(tupla_imiona)
# name1, name2, name3
name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)  # Radek Tomek ['Zenek', 'Marcin', 'Ania', 'Zosia']

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)  # Radek ['Tomek', 'Zenek', 'Marcin', 'Ania'] Zosia

*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)  # ['Radek', 'Tomek', 'Zenek', 'Marcin'] Ania Zosia

tupla_lista = list(tupla_imiona)
print(tupla_lista)  # ['Radek', 'Tomek', 'Zenek', 'Marcin', 'Ania', 'Zosia']
print(type(tupla_lista))  # <class 'list'>

print("Radek" in tupla_lista)  # True
