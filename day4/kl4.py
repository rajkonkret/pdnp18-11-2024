class Ptak:
    """
    kalsa opisująca Ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca (konstruktor)
        :param gatunek:
        :param szybkosc:
        """

        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)


class Kura(Ptak):
    """
    Klasa Kura dziedziczy z klasy Ptak
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")


class Orzel(Ptak):
    """
    Klasa Orzel dziedziczy z Ptak
    """


or1 = Ptak("Orzeł", 45)
or1.latam()  # Tu Orzeł Lecę z szybkością 45
kur1 = Ptak("Kura", 0)
kur1.latam()  # Tu Kura Lecę z szybkością 0

kur2 = Kura("Kura domowa")
kur2.latam()  # Tu Kura domowa Ja nie latam.
or2 = Orzel("Orzel bielik", 50)
or2.latam()  # Tu Orzel bielik Lecę z szybkością 50
