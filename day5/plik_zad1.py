# działania z plikami
# context manager - dba o bezpieczenstwo przy dostepie do zasobów
# with - context manager w pythonie
# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', 'w', encoding='utf-8') as fh:
    fh.write("Powitanie\n")
    fh.write("Drugie\n")
    fh.write("Kolejne\n")

# FileExistsError: [Errno 17] File exists: 'test.log'
# 'x' - jesli plik istnieje dostaniemy bład
# with open('test.log', 'x', encoding='utf-8') as file:
#     file.write("Zapisz\n")

# 'w' jesli plik istnieje zostanie skasowany !!!
with open('test.log', 'w', encoding='utf-8') as f:
    f.write("Nadpisane\n")

# 'a' dopisanie na końcu pliku
with open('test.log', 'a', encoding='utf-8') as file:
    file.write("Dopisane\n")
    file.write("Dopisane\n")
    file.write("Dopisane\n")
    file.write("Dośdane\n")

# shift enter - otworzenie w nowym oknie

with open('test.log', 'r', encoding='utf-8') as f:
    lines = f.read()

print(lines)
# Nadpisane
# Dopisane
# Dopisane
# Dopisane
