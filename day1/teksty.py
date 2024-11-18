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
tekst_upper = tekst.upper() # do zmiennej przechwytujemy zmieniony tekst
print(tekst_upper)  # WITAJ ŚWIECIE

tekst_lower = tekst.lower()
print(tekst_lower)  # witaj świecie