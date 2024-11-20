# wyjątki - błedy generowane podczas działania programu

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdnp18-11-2024\day3\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

try:
    # print(5 / 0)
    # print("A" + 9)
    # print(int("A"))
    # raise KeyError("Nie ma klucza")
    wynik = 90 / 34
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Bład typu")
except ValueError:
    print("Bład wartości")
except Exception as e:  # pozostałe błędy
    print("Bład", e)  # Bład 'Nie ma klucza'
else:  # tylko gdy nie ma błedu
    print("Wynik", wynik)
finally:  # wykona się zawsze niezależnie od błedu
    print("Następny proszę...")

print("Program nadal działą")
# Nie dziel przez zero
# Program nadal działą
# Bład wartości
# Program nadal działą
# Bład 'Nie ma klucza'
# Program nadal działą
# Wynik 2.6470588235294117
# Program nadal działą
# Wynik 2.6470588235294117
# Następny proszę...
# Program nadal działą
# try except [else - finally]
