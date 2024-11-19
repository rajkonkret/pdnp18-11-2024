import sys  # zaimportowalismy biblioteke sys

user = "Tomek"  # str
wiek = 39  # int
wersja = 3.90001  # liczba zmiennoprzecinkowa, <class 'float'>
print(type(wersja))  # <class 'float'>
liczba = 567890123456  # int
print(type(liczba))  # <class 'int'>

print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)

print("Witaj %s, masz teraz %d lat." % (user, wiek))  # Witaj Tomek, masz teraz 39 lat.
# print("Witaj %d, masz teraz %s lat." % (user, wiek))# Witaj Tomek, masz teraz 39 lat.
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdnp18-11-2024\day2\formaty.py", line 17, in <module>
#     print("Witaj %d, masz teraz %s lat." % (user, wiek))# Witaj Tomek, masz teraz 39 lat.
#           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~
# TypeError: %d format: a real number is required, not str
# za %d musimy podstawić liczbę - sprawdza typy

print("Witaj {}, masz teraz {} lat.".format(user, wiek))  # Witaj Tomek, masz teraz 39 lat.

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.
# f - fstring, tekst sforamtowany

print("Uzywamy wersji Pythona %i" % 3)  # Uzywamy wersji Pythona 3
print("Uzywamy wersji Pythona %f" % 3)  # Uzywamy wersji Pythona 3.000000
print("Uzywamy wersji Pythona %.2f" % 3.9)  # Uzywamy wersji Pythona 3.90
print("Uzywamy wersji Pythona %.1f" % 3.9)  # Uzywamy wersji Pythona 3.9
print("Uzywamy wersji Pythona %.0f" % 3.9)  # Uzywamy wersji Pythona 4 - zaokrągli przy wyswietlaniu
print("Uzywamy wersji Pythona %.f" % 3.9)  # Uzywamy wersji Pythona 4 - zaokrągli

x = 3.8764
print("Wynik = %.2f" % x)  # Wynik = 3.88
print("Liczba x:", x)  # Liczba x: 3.8764, liczba nie zostaje zmieniona
print(3.9 * 3.9)  # 15.209999999999999
print("%.f" % (3.9 * 3.9))  # 15

print(f"Uzywamy pythona {wersja}")  # Uzywamy pythona 3.90001
print(f"Uzywamy pythona {wersja:.1f}")  # Uzywamy pythona 3.9
print(f"Uzywamy pythona {wersja:.2f}")  # Uzywamy pythona 3.90
print(f"Uzywamy pythona {wersja:.0f}")  # Uzywamy pythona 4
# print(f"Uzywamy pythona {wersja:.f}")  # ValueError: Format specifier missing precision

print(f"{user:>10}")  # "     Tomek" - wyrównanie do prawej, uzupełnia do długości 10 znaków
print(f"{user:<15}")  # "Tomek          " - wyrównanie do lewej
print(f"{user:^20}")  # "       Tomek        " - wycentrowanie

print(liczba)  # 567890123456
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 567,890,123,456
print(f"Nasza duża liczba {liczba:_}")  # Nasza duża liczba 567_890_123_456
print(f"Nasza duża liczba {liczba:,}".replace(",", "."))  # Nasza duża liczba 567.890.123.456
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))  # Nasza duża liczba 567 890 123 456

liczba_2 = 15_000_000_000
# liczba_2 = 15000000000
print(type(liczba_2))
print(liczba_2)
# <class 'int'>
# 15000000000
