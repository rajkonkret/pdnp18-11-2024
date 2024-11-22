import csv

fields = []
rows = []

# filename = 'records_dict.csv'
filename = 'records_dict_list.csv'

# ctrl ] - kursor na koniec wiersza
with open(filename, "r") as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    print(dialect.delimiter)  # ;
    print(dialect.quotechar)  # "
    print(dialect.quoting)
    print(dialect.doublequote)
    f.seek(0)  # wróc na początek pliku
    # csvreader = csv.reader(f, delimiter=";")
    csvreader = csv.reader(f, delimiter=dialect.delimiter)

    print(csvreader)  # <_csv.reader object at 0x0000017CFC7FE860>, iterator

    fields = next(csvreader)  # odczytanie jedego wiersza,
    for row in csvreader:  # zaczyna odczyt od kolejnego wiersza
        # print(row)
        rows.append(row)

print("Nazwy kolumn:", fields)
print("wiersze:", rows)
# Nazwy kolumn: ['name', 'braanch', 'year', 'cgpa']
# wiersze: [['radek', 'coe', '2', '9.1']]

# <_csv.reader object at 0x000001571CE0E8C0>
# Nazwy kolumn: ['sku', 'exp_date', 'price']
# wiersze: [['1', 'today', '100'], ['2', 'today', '200'], ['3', 'tomorrow', '300'], ['4', 'today', '50'], ['5', 'today', '99.99']]
