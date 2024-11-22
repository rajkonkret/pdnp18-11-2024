# nosql i sql -  nierelacyjne, relacyjne,
import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Baza danych podłaczona")
except sqlite3.Error as e:
    print("Bład", e)
finally:
    if conn:
        conn.close()
        print("Połaczenie zostało zamknięte")

# Baza danych podłaczona
# Połaczenie zostało zamknięte
