# {"name":"John", "age":30, "car":null}
# dane typu klucz wartość
# uzywany jest do komunikacji w internecie
# odpowiednikiem jsona w pythonie jest słownik

import json
from operator import index

person_dict = {'name': "Radek", 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f)

# upiększanie jsona
with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# posortowany po kluczach
with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
    # {
    #     "age": 40,
    #     "czy_pali": null,
    #     "name": "Radek"
    # }

# odczytane z pliku i przekształcone na słownik
with open('nasze_dane.json', 'r') as file:
    data = json.load(file)

print(data)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(data))  # <class 'dict'>
print(data['name'])  # odczyt ze słownika, Radek

# zamiana słownika na json
json_text = json.dumps(data)
print(json_text)  # {"age": 40, "czy_pali": null, "name": "Radek"}
print(type(json_text))  # <class 'str'>

dict_json = json.loads(json_text)
print(dict_json)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(dict_json))  # <class 'dict'>

# wypisac ze słownika klucze i wartości, wstawic własny separator
for key, value in dict_json.items():
    print(key, value, sep=" <=> ")
# age <=> 40
# czy_pali <=> None
# name <=> Radek
