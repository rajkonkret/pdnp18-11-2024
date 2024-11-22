# pliki csv - dane oddzielone znakiem podziału (,;tab)
# Year,Make,Model
# 1997,Ford,E350
# 2000,Mercury,Cougar
import csv

row = ['radek', 'coe', 2, '9.1']
fields = ['name', 'braanch', 'year', 'cgpa']

dictionary = dict(zip(fields, row))
print(dictionary)
# {'name': 'radek', 'braanch': 'coe', 'year': 2, 'cgpa': '9.1'}

filename = 'records.csv'
with open(filename, 'w', newline='') as csv_f:
    csvwriter = csv.writer(csv_f)  # narzędzie do zapisywania pliku csv
    csvwriter.writerow(fields)  # zapis wiersza
    csvwriter.writerow(row)  # zapis wiersza

#  newline='' - obejscie problemu podwójnego znaku końca linii

filename = "records_dict.csv"
with open(filename, 'w', newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()  # zapisz nazwy kolumn
    csvwriter.writerow(dictionary)

products = [
    {'sku': 1, 'exp_date': 'today', 'price': 100},
    {'sku': 2, 'exp_date': 'today', 'price': 200},
    {'sku': 3, 'exp_date': 'tomorrow', 'price': 300},
    {'sku': 4, 'exp_date': 'today', 'price': 50},
    {'sku': 5, 'exp_date': "today", 'price': 99.99},
]

filename = "records_dict_list.csv"
# fields_product = ['sku', 'exp_date', 'price']
fields_product = [k for k in products[0]]  # wyciąga klucze ze słownika

with open(filename, 'w', newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields_product, delimiter=";")
    csvwriter.writeheader()  # zapisz nazwy kolumn
    csvwriter.writerows(products)  # lista słowników

# delimiter=";" - znak podziału
