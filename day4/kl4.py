from abc import ABC, abstractmethod


class Ptak(ABC):
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

    # oznaczamy metode jako abstrakcyjna
    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    """
    Klasa Kura dziedziczy z klasy Ptak
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def wydaj_odglos(self):
        print("ko ko ko ko ko ko")


class Orzel(Ptak):
    """
    Klasa Orzel dziedziczy z Ptak
    """

    def wydaj_odglos(self):
        print("kier kir kier")

# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
class Sowa(Ptak):
    """
    Klasa Sowa dziedziczy po klasie Ptak
    """


# nie można stworzyc obiektu klasy abstrakcyjnej
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzeł", 45)
# or1.latam()  # Tu Orzeł Lecę z szybkością 45
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0

kur2 = Kura("Kura domowa")
kur2.latam()  # Tu Kura domowa Ja nie latam.
or2 = Orzel("Orzel bielik", 50)
or2.latam()  # Tu Orzel bielik Lecę z szybkością 50

or2.wydaj_odglos()
kur2.wydaj_odglos()
# kier kir kier
# ko ko ko ko ko ko

# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
# bo ni e ma metody wydaj_odglos
# sowa = Sowa("Sowa", 15)
