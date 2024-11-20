# od pythona 3.10
# match case

lista = []  # tworzymy pustą listę
lang = input("Podaj znany Ci język programowania")

match lang.casefold().strip():
    case "python":
        lista.append("Znam Pythona")
    case "java":
        lista.append("java")  # dodaj do listy
    case _:
        print("Nie znam takiego języka")

print(lista)
# Podaj znany Ci język programowaniajava
# ['java']
