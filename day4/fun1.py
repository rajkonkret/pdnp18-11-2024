# funkcje - wykonuje fragment kodu w dowolnym momencie
# funkcja musi byc najpierw zadeklarowana
# w miejscu deklaracji funkcja się nie wykonuje!!!
# żeby funkcja się wykonała trzeba ją wywołać

a = 6
b = 8


# te funkcje nie zwracają wyniku

# PEP8 zaleca by funkcję od reszty programu oddzielały dwie puste linie
# deklaracja funkcji
# funkcja bez argumentów
def dodaj():
    print(a + b)


def dodaj2(a, b):  # obowiązkowe argumenty
    print(a + b)


def odejmij(a, b, c=0):  # c=0 domyślna wartość
    print(a - b - c)


# wywołanie funkcji - nazwa funkcji i nawiasy ()
dodaj()  # wyświetli 14
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(67, 89)  # 156
# shift tab - cofnięcie tabulatora
# przekazywanie argumentów po pozycji
odejmij(1, 2, 3)  # -4, 1 - 2 - 3
odejmij(1, 2)

# przekazanie argumentów po nazwie
odejmij(c=10, b=90, a=345)  # 245, 345 - 90 - 10  = 245
odejmij(b=9, a=99)  # 90

# mieszane
odejmij(1, c=10, b=30)  # -39
odejmij(1, b=8)  # -7

# pozycyjne muszą byc przed nazwanymi
# odejmij(b=9,4) #                  ^
# SyntaxError: positional argument follows keyword argument

print(dodaj())
# 14
# None

# None + None
# print(dodaj() + dodaj2(6, 8)) TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
