# kolekcje
# lista - przechowuje dowolną ilość danych
# może przechowywac rózne typy na raz, int, str w jedej liscie
# zachowuje kolejnośc przy dodawaniu elementów
from sys import base_prefix

# pusta lista
lista = []
print(type(lista))  # <class 'list'>
print(lista)  # []

pusta_lista = list()
print(type(pusta_lista))  # <class 'list'>
print(pusta_lista)  # []

# append() - dodawanie elementów na końcu listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Paweł")
lista.append("Grzegorz")
lista.append("Aneta")
lista.append("Zenek")
print(lista)  # ['Radek', 'Tomek', 'Paweł', 'Grzegorz', 'Aneta', 'Zenek']

# ['Radek', 'Tomek', 'Paweł', 'Grzegorz', 'Aneta', 'Zenek']
#     0        1         2        3          4        5
#     -6       -5       -4        -3         -2       -1
print(lista[0])  # Radek
print(lista[2])  # Paweł
print(lista[4])  # Aneta

print(len(lista))  # lista posiada 6 elementów
# print(lista[6])  # IndexError: list index out of range, nie ma takiego indeksu

print(lista[-1])  # ostatni element
print(lista[len(lista) - 1])
print(lista[-2])  # Aneta
print(lista[-3])  # Grzegorz

# wyświetlanie fragmentów listy (slicowanie)
print(lista[0:3])  # [start:stop] ['Radek', 'Tomek', 'Paweł'] indeksy 012
print(lista[:3])  # ['Radek', 'Tomek', 'Paweł']
print(lista[2:])  # ['Paweł', 'Grzegorz', 'Aneta', 'Zenek'] do końca włącznie
print(lista[2:5])  # ['Paweł', 'Grzegorz', 'Aneta'] indeksy 234

print(lista[2:10])  # ['Paweł', 'Grzegorz', 'Aneta', 'Zenek']
print(lista[10:20])  # [] - pusta lista
print(lista[2:2])  # []
print(lista[2:3])  # ['Paweł']
print(lista[:])

print(type(lista[2]))  # <class 'str'>
print(type(lista[2:3]))  # <class 'list'>

# ['Radek', 'Tomek', 'Paweł', 'Grzegorz', 'Aneta', 'Zenek']
#     0        1         2        3          4        5
#     -6       -5       -4        -3         -2       -1
print(lista[-2:0])  # [] -> [4:0]
print(lista[0:-2])  # ['Radek', 'Tomek', 'Paweł', 'Grzegorz'], [0:4]

lista_15 = list(range(15))  # range() generuje liczby od 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(lista_15[0:15:2])  # [start:koniec:krok], [0, 2, 4, 6, 8, 10, 12, 14]
print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14]
print(lista_15[-10])  # 5

# nadpisanie elementu w liście
lista[3] = "Mikołaj"
print(lista)  # ['Radek', 'Tomek', 'Paweł', 'Mikołaj', 'Aneta', 'Zenek']

# dopisanie elementu we wskazanym indeksie
lista.insert(1, "Marcin")
print(lista)  # ['Radek', 'Marcin', 'Tomek', 'Paweł', 'Mikołaj', 'Aneta', 'Zenek']
print(len(lista))  # długośc 7

# sprawdzenie indeksu dla danego elementu
print(lista.index("Tomek"))  # indeks numer 2

# usunięcie elementu z listy, pierwsze wystąpienie
lista.append("Zenek")
lista.append("Zenek")
print(lista)
# ['Radek', 'Marcin', 'Tomek', 'Paweł', 'Mikołaj', 'Aneta', 'Zenek', 'Zenek', 'Zenek']

print(lista.remove("Zenek"))  # remove() - usunięcie elementu
print(lista)
# ['Radek', 'Marcin', 'Tomek', 'Paweł', 'Mikołaj', 'Aneta', 'Zenek', 'Zenek']

# usunięcie po indeksie, zwraca co usunęła
print(lista.pop(5))  # Aneta
print(lista)  # ['Radek', 'Marcin', 'Tomek', 'Paweł', 'Mikołaj', 'Zenek', 'Zenek']
print(lista.pop(-2))  # Zenek
print(lista.pop())  # Zenek, ostatni element z listy
print(lista)  # ['Radek', 'Marcin', 'Tomek', 'Paweł', 'Mikołaj']

a = 1
b = 3
a = b
print(a, b)  # 3 3
print(f"{a=}, {b=}")
# a = 3, b = 3

b = 7
print(f"{a=}, {b=}")

lista_2 = lista  # a = b, kopia referencji, adres w pamięci

print(lista)
print(lista_2)
# ['Radek', 'Marcin', 'Tomek', 'Paweł', 'Mikołaj']
# ['Radek', 'Marcin', 'Tomek', 'Paweł', 'Mikołaj']
lista_copy = lista.copy()
lista.clear()  # clear() usuń wszystkie elementy z listy
print(lista)  # []
print(lista_2)  # []
print(lista_copy)  # []
print(id(lista))
print(id(lista_2))
print(id(lista_copy)) # ['Radek', 'Marcin', 'Tomek', 'Paweł', 'Mikołaj']
# 2379788915072
# 2379788915072
# 2379792596736
