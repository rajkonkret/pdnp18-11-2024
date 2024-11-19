tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# Witaj Świecie
# <class 'str'>

# wszystko jest obiektem
tekst.upper()
""" Return a copy of the string converted to uppercase. """
print(tekst)
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()  # do zmiennej przechwytujemy zmieniony tekst
print(tekst_upper)  # WITAJ ŚWIECIE

tekst_lower = tekst.lower()
print(tekst_lower)  # witaj świecie

# Witaj Świecie
# 0123456789012
print(tekst.count("i"))  # występuje 3 razy, sprawdza cały tekst
print(tekst.count("j", 0, 4))  # występuje 0 razy, z prawej zbiór otwarty, indeksy 0123
print(tekst.count("j", 0, 4))
# tego x: __start __end nie piszemy. To tylko podpowiedź
# Wita
# 0123

print(tekst.removesuffix("Świecie"))  # "Witaj "
print(tekst.removeprefix("Witaj"))  # " Świecie"

tekst_zamiana = "Witaj dobry Świecie"
print(tekst_zamiana.replace("dobry", " "))  # Witaj   Świecie
print(tekst_zamiana.replace("dobry ", " "))  # Witaj  Świecie

# strip() - usunięcie białych znków i spacji na początku i końcu tekstu
print(tekst.removeprefix("Witaj").strip())  # "Świecie"
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

print(tekst[4])  # indeks numer 4, literka "j"

encode_s = tekst.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie'
print(type(encode_s))  # <class 'bytes'>, typ bajtowy
# \xc5\x9 - zapis szesnastkowy, \xc5 - 197
print(encode_s.decode('utf-8'))  # Witaj Świecie
