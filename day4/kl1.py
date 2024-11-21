# klasy - element programowania obiektowego
# klasa - szablon, przepis
# klasa wyznacza minimum cech jakie powinen posiadac obiekt
# obiekt ma cechy - zmienne
# funkcje - metody
# klasa musi byc najpierw zdefiniowana
# definicja klasy nie uruchamia nic
# budowanie obiektu klasy (instancji) uruchamia metode inicjalizującą
# paradygmaty programowania obiektowego
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja


# deklaracja klasy, tu sie nic nie wykonuje
# PEP8 zaleca by do nazw klas uzywac dużej litery PascalCase
class Human:
    """
    Klasa Human w pythonie
    """

    imie = ""
    wiek = None
    plec = "k"


# wypisanie dokumentacji klasy Human
print(Human.__doc__)  # Klasa Human w pythonie
print(print.__doc__)

# tworzymy obiekt tej klasy
cz1 = Human()
print(cz1)  # <__main__.Human object at 0x00000236A4B03770>

print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# #
# None
# k

cz1.imie = "Anna"
cz1.wiek = 45
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Anna
# 45
# k

# drugi obiekt o nazwie cz2
cz2 = Human()
cz2.imie = "Radek"
cz2.wiek = 49
cz2.plec = "m"
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
# Radek
# 49
# m

# przejscie do katalogu cd day4
# cd .. wyjscie w gore
# cd.\day4\
# pydoc -b - uruchomienie serwera z dokumentacją