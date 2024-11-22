import csv

fields = []
rows = []

filename = 'records_dict.csv'

# ctrl ] - kursor na koniec wiersza
with open(filename, "r") as f:
    csvreader = csv.reader(f)

    print(csvreader)  # <_csv.reader object at 0x0000017CFC7FE860>, iterator

    fields = next(csvreader)  # odczytanie jedego wiersza,
    for row in csvreader:  # zaczyna odczyt od kolejnego wiersza
        # print(row)
        rows.append(row)

print("Nazwy kolumn:", fields)
print("wiersze:", rows)
# Nazwy kolumn: ['name', 'braanch', 'year', 'cgpa']
# wiersze: [['radek', 'coe', '2', '9.1']]

