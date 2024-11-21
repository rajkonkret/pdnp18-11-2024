# a=1 - argumenty nazwane
def connect(**opcje):  # ** dowolna ilosc argumentów nazwanch
    print(opcje)
    print(type(opcje))


connect()
# {}
# <class 'dict'> słownik

connect(a=1)
# {'a': 1}
# <class 'dict'>
connect(a=1, name="Radek", age=37)


# {'a': 1, 'name': 'Radek', 'age': 37}
# <class 'dict'>

def all_params(*args, **kwargs):
    print(args, kwargs)


all_params()  # () {}
all_params(1, 2, 3, 4, 5)  # (1, 2, 3, 4, 5) {}
all_params(a=10, name="Aneta")  # () {'a': 10, 'name': 'Aneta'}
all_params(1, 2, 3, a=10, b=30, name='Tomek')  # (1, 2, 3) {'a': 10, 'b': 30, 'name': 'Tomek'}
