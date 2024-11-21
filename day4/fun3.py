a = 10
b = 10


def dodaj():
    a = 7  # lokalne argumenty
    b = 8  # nie mzieniaja wartości globalnych
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a  # uzyj globalnego
    a = 9  # nadpisuje globalne a
    b = 89
    print(a + b)


print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=10 (globalna)
dodaj()  # 15
print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=10 (globalna)
dodaj2()  # 20
print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=10 (globalna)
dodaj3()  # 98
print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=9 (globalna)
dodaj2()  # 19
print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=9 (globalna)
