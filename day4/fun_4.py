# stworzyc funkcję obliczającą średnią

def srednia(*cyfry):  # *cyfry , dowolna ilośc argumentów po pozycji 1,2,3,4,5...
    print(cyfry)  # ()
    count = len(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Średnia awynosi {avg}")
    finally:
        print("Kolejny uczeń")
# ()
# Bład division by zero
# Kolejny uczeń
# (1, 2)
# Średnia awynosi 1.5
# Kolejny uczeń
# (4, 5, 6, 5, 6)
# Średnia awynosi 5.2
# Kolejny uczeń
# (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Średnia awynosi 5.0
# Kolejny uczeń

srednia()
srednia(1, 2)
srednia(4, 5, 6, 5, 6)
srednia(1, 2, 3, 4, 5, 6, 7, 8, 9)
# ()
# (1, 2)
# (4, 5, 6, 5, 6)
# (1, 2, 3, 4, 5, 6, 7, 8, 9)
