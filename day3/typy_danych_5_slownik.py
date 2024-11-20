# słownik - dane typu para klucz-wartosc
# {'user' : 'Radek', 'wiek': 78}
# {"klucz":"wartosc"}
# odpowiednik jsona {"name":"John", "age":30, "car":null}
# nie mogą się powtórzyć klucze

# pusty słownik
dictionary = dict()
print(type(dictionary))  # <class 'dict'>
print(dictionary)  # {}

dictionary_1 = {}
print(type(dictionary_1))  # <class 'dict'>
print(dictionary_1)  # {}

# dodanie elementów do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 38
print(dictionary)  # {'imie': 'Radek', 'wiek': 38}

# nadpisanie elementu
dictionary['imie'] = 'Tomek'
print(dictionary)
# {'imie': 'Radek', 'wiek': 38}
# {'imie': 'Tomek', 'wiek': 38}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Tomek', 38])
print(dictionary.items())  # dict_items([('imie', 'Tomek'), ('wiek', 38)])

# wypisanie elementu ze słownika
print(dictionary['imie'])  # Tomek
print(dictionary['wiek'])  # 38

# print(dictionary['Imie']) # KeyError: 'Imie' bład klucza
print(dictionary.get("Imie"))  # None takiego klucza w słowniku nie ma, program nadal działa
print(dictionary.get("Imie", 'Default'))  # Default

dictionary.update({"date": '12-12-2024'})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 38, 'date': '12-12-2024'}

dict_small = {'x': 2}
dict_small.update([('y', 3), ("z", 7)])  # dodanie danych do słownika w postaci krotek (klucz, wartosc)
print(dict_small)  # {'x': 2, 'y': 3, 'z': 7}
