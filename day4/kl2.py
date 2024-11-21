class Human:
    """
    klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        # self - obiekt na którym pracujemy
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def ruszaj(self):
        if self.plec == "m":  # cz1.plec ?
            print("Ruszyłem w drogę")
        else:
            print("Ruszyłam w drogę")


# cz1 = Human() # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Anna", "34", 168)
print(cz1.imie)
print(cz1.wiek)
print(cz1.wzrost)
print(cz1.plec)
# Anna
# 34
# 168
# k

cz2 = Human("Radek", 49, 193, "m")
print(cz2.imie)  # Radek
print(cz2.wiek)  # 49
print(cz2.wzrost)  # 193
print(cz2.plec)  # m

cz1.ruszaj()
cz2.ruszaj()
# Ruszyłam w drogę
# Ruszyłem w drogę
