print()
# Process finished with exit code 0 - program zakończony poprawnie

print("Nazywam się Radek")
print('Nazywam się Radek')
print('Nazywam się Radek')
# ctrl d - powielanie linijki
# Nazywam się Radek
# Nazywam się Radek
# ctrl / - automatyczny komentarz
# ctrl alt l - formatowanie

# sprawdzenie jakiego typu to są dane
# type()
print(type("Radek"))  # <class 'str'>, string, typ tekstowy
print("39")  # 39
print(type("39"))  # <class 'str'>

print(39)  # 39
print(type(39))  # <class 'int'>, integer, liczby całkowite
# ctrl shift f10 - uruchamianie

# PEP8
print(39 + 39)  # 78
print("39" + "39")  # 3939, konkatenacja, łaczenie stringów

# print(39 + "39")
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdnp18-11-2024\day1\pierwszy.py", line 27, in <module>
#     print(39 + "39")
#           ~~~^~~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# ctrl / (klawisz z ?) dodanie komentarza

# int() rzutowanie, zamiana tekstu na liczbę
print(int("39") + 39)  # 78

# str() - zamiana na str
print("Radek" + str(39))  # Radek39, połączył stringi

print(5 * "4")  # 44444 powielona 4
print("160" * 25)
# 160160160160160160160160160160160160160160160160160160160160160160160160160
print(160 * 25)  # 4000

# zmienna - pudełko dane
# przechowuje jeden element
# snake_case
# nazwa zmiennej powinna wslazywać co przechowuje
liczba = 39
print(liczba)  # 39, wypisanie zawartości zmiennej, nazwa zmiennej bez cudzysłowiów

# typowanie dynamiczne
name = "Radek"
print(name)  # Radek
print(type(name))  # <class 'str'>

name = 90
print(name)
print(type(name))
# 90
# <class 'int'>

# print(name + "Kowalski")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

name: str = "Radek"  # :str to tylko podpowiedz typu
print(name)
name = 90
print(name)
# Radek
# 90

age = 38
print(age)
print(type(age))
# 38
# <class 'int'>
