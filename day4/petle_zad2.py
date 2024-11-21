dictionary = {'imie': 'Radek', 'nazwisko': "Kowalski"}  # słownik

# wypisze klucze
for k in dictionary:
    print(k)
# imie
# nazwisko

for k in dictionary.keys():
    print(k)
    # imie
    # nazwisko

# wypisze wartosc
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wyświetli pary, jako krotkę (tuple)
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)

# imie => Radek
# nazwisko => Kowalski
#  sep
#         string inserted between values, default a space.

# nadpisujemy seperator
for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>Kowalski

# end
#         string appended after the last value, default a newline.
# nadpisany znak końca linii, nie przechodzi do nowej
for k, v in dictionary.items():
    print(k, "=>", v, end=" ;;;; ")
    # imie => Radek ;;;; nazwisko => Kowalski ;;;;
# tu nadal obowiązuje     end=" ;;;; "
print("Radek")  # imie => Radek ;;;; nazwisko => Kowalski ;;;; Radek
# tu juz ustawiony domyslny znak końca linii
print("Tomek")  # wypisze w nowej linii
# imie => Radek
# nazwisko => Kowalski
# imie=>Radek
# nazwisko=>Kowalski
# imie => Radek ;;;; nazwisko => Kowalski ;;;; Radek
# Tomek

pol_ang = {'kot': 'cat', 'pies': 'dog'}
ang_pol = {}
for k, v in pol_ang.items():  # pobierze pary po kolei
    ang_pol[v] = k

print(ang_pol)  # {'cat': 'kot', 'dog': 'pies'}
print({value: key for key, value in pol_ang.items()})
# {'cat': 'kot', 'dog': 'pies'}
