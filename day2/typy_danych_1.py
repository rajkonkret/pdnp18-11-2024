import sys

wiek = 47  # int
rok = 2024  # int
temp = 36.6  # float

print(temp)
print(type(temp))  # <class 'float'>

print(wiek * rok)  # 95128
print(wiek - rok)  # -1977
print(wiek + rok)  # 2071
print(wiek / rok)  # 0.023221343873517788

print(rok // wiek)  # częśc calkowita dzielenia 43
print(rok % wiek)  # modulo, reszta z dzielenia
print(10 % 3)  # 3 całe, reszty 1
print(4 % 2)  # reszta 0, liczba parzysta

print(wiek ** rok)

# len() długość
print(len(str(wiek ** rok)))  # długośc wynosi 3385 znaków
# print(len(str(wiek ** rok ** 2)))  #ValueError: Exceeds the limit (4300 digits)
# for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 8 / 2 + 8 / 2)  # -153.0
print(54 - 5 * 43 + (8 / 2 + 8) / 2)  # -155.0

# floaty posiadają bład zaokrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
#  x=SMB^{E}
# , the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308,
#                max_exp=1024,
#                max_10_exp=308,
#                min=2.2250738585072014e-308,
#                min_exp=-1021,
#                min_10_exp=-307,
#                dig=15,
#                mant_dig=53,
#                epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(f"Sprawdzenie zmiennych {temp} {wiek} {rok}")  # Sprawdzenie zmiennych 36.6 47 2024
print(f"""
{wiek} {rok}""")
# "
# 47 2024"

# typ logiczny, boolean
# prawda fałsz
# True False - z dużej literami
# 1 - prawda, 0 - fałsz

czy_znasz_pythona = True
print(type(czy_znasz_pythona))  # <class 'bool'>, typ logiczny
print(czy_znasz_pythona)  # True

print(int(True))  # 1
print(int(False))  # 0

print(bool(1))  # bool() zamiana (rzutowanie) na typ logiczny, True
print(bool(100))  # True
print(bool(-10))  # True
print(bool("radek"))  # True

print(bool(0))  # False
print(bool(""))  # False
print(bool(None))  # None - nic, stan nieokreslony, nie wiem -> null w innych systemach

print(bool(" "))  # True
print(bool())  # False

# działąnia logiczne
# and - i
# Expression    Evaluates to
# True and True    True
# True and False    False
# False and True    False
# False and False    False

# or - lub
# The or Operator’s Truth Table:
#
# Expression    Evaluates to
# True or True    True
# True or False    True
# False or True    True
# False or False    False
# The not Operator’s Truth Table:
#
# Expression    Evaluates to
# not True    False
# not False   True
# and, or, not

print(False and True)  # False

print(False or True)  # True

print(not False)  # True

a = 8
b = 6
# f - fstring, w klamerkach {} zostanie wpisana wartość zmiennej
print(f"Porównanie {a} > {b} = {a > b}")  # Porównanie 8 > 6 = True
print(f"Porównanie {a} < {b} = {a < b}")  # Porównanie 8 < 6 = False
print(f"Porównanie {a <= b = }")  # Porównanie a <= b = False
print(f"Porównanie {a >= b = }")  # Porównanie a >= b = True
print(f"Porównanie {a} == {b} = {a == b}")  # == porównanie, czy a równa się b,Porównanie 8 == 6 = False
print(f"Porównanie {a} != {b} = {a != b}")  # != porównanie, czy a różne od b, Porównanie 8 != 6 = True
# typy primitywne - str, int, bool, float
