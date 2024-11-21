# while - pętla sterowana warunki

# pętla nieskończona
# while True:
#     print("Komunikat 1 !")

licznik = 0
while True:
    licznik += 1  # licznik = licznik + 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # przerwanie pętli

print(licznik)  # 11

licznik = 0
while licznik < 10:
    licznik += 1
    print("komunikat 3 !!!")

# password = input("Podaj hasło")
# while password != 'secret':
#     password = input("Błędne hasło. Podaj ponownie")
# print("Hasło prawidłowe")
# Podaj hasło4
# Błędne hasło. Podaj ponownierewr
# Błędne hasło. Podaj ponownieweqweq
# Błędne hasło. Podaj ponownieasdasd
# Błędne hasło. Podaj ponowniesddadsd
# Błędne hasło. Podaj ponowniesecret
# Hasło prawidłowe

# A string is numeric if all characters in the string are numeric
lista = []
lista_int = []
while True:
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))  # int() - rzutowanie na int

print(lista)  # ['3', '4', '6', '12', '23', '890', '123', '4444']
print(lista_int)
# ['5', '6', '7', '12', '234', '56', '098'] str
# [5, 6, 7, 12, 234, 56, 98] int

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
print(5 in my_list)  # True, sprawdzenie czy element jest w liscie
while 5 in my_list:
    my_list.remove(5)

print(my_list)  # [1, 2, 3, 4, 6]
# alt shift E - uruchomienie fragmentu kodu
