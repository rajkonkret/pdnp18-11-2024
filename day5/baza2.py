# nosql i sql -  nierelacyjne, relacyjne,
import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Baza danych podłaczona")

    # query = '''
    # CREATE TABLE IF NOT EXISTS developers (
    # id INTEGER PRIMARY KEY,
    # name TEXT NOT NULL,
    # salary REAL NOT NULL);
    # '''
    #
    # c.execute(query)
    # conn.commit() # zapamiętaj zmiany

    # insert = """
    # INSERT INTO developers (id,name,salary) VALUES (1,'Radek','15000');
    # """
    #
    # c.execute(insert)
    # conn.commit()

    select = '''
    SELECT * FROM developers;
    '''

    for row in c.execute(select):
        print(row)  # (1, 'Radek', 15000.0)

except sqlite3.Error as e:
    print("Bład", e)
finally:
    if conn:
        conn.close()
        print("Połaczenie zostało zamknięte")

# Baza danych podłaczona
# Połaczenie zostało zamknięte
