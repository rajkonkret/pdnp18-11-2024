# warunki - instrukcje warunków
# instrukcje sterowania przepływem
# w zależności od warunku (True Fale) wykona jeden lub drugi blok(fragment) programu
# warunek musi zwracac typ bool -> boolean, typ logiczny
# if

odp = True
print(bool(odp))  # True
odp = False
if odp:
    # obowiązkowe 4 spacje
    # wykona się tylko gdy warunek bedzie True
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza część programu")
# True
# Brawo
# Brawo
# Brawo
# Brawo
# Brawo
# Dalsza część programu

odp = "Radek"
print(bool(odp == "Radek"))  # True
if odp == "Radek":
    print("Radek")  # Radek

if odp == "Tomek":
    print("To jest Tomek")
else:  # w przeciwnym przypadku
    print("To nie jest Tomek")
# To nie jest Tomek

# napisać aplikację Test
# zadac pytanie
# pobrac odpowiedz
# wypisac wynik prawidłowa/nieprawidłowa odpowiedź

# punkty = 0
# odp = input("Podaj rok Bitwy pod Grunwaldem")
# if odp == '1410':
#     print("Prawidłowo")
#     punkty += 1  # punkty = punkty + 1
# else:
#     print("Musisz uczyć się dalej")
# # Podaj rok Bitwy pod Grunwaldem1410
# # Prawidłowo
# print("Punkty", punkty)

# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

suma_zam = 150
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabat wynosi {rabacik}")  # Rabat wynosi 25

rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25
# f - fstring, sformatowany string
#
# podatek = 0
# zarobki = int(input("Podaj zarobki"))
#
# if zarobki < 10000:
#     podatek = 0
# elif zarobki < 29999:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi {podatek * zarobki}")
# jak dodac podatek 0.2, dla przedziału 10000 do 29999
# wykonywane w kolejności
# pierwszy True , wychodzi z drzewka
# Podaj zarobki50000
# Podatek wynosi 20000.0

system_alert = "email"  # email, console
error = "error"
lista_b = []

if system_alert == "console":
    print("Stało się coś strasznego")
elif system_alert == "email":
    print("Sytem email")
    if error == "error":
        lista_b.append("Krytyczny")
    elif error == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("inny")
else:
    print("nie znam takiego systemu")

print(lista_b)
# Sytem email
# ['Krytyczny'] - wypisane z listy