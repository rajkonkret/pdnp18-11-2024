from datetime import date, datetime, timedelta

today = date.today()
print(today)  # 2024-11-21
print(type(today))  # <class 'datetime.date'>, specjalny typ dla dat

time = datetime.now()
print(time)  # 2024-11-21 10:42:25.647694

formatted_date = datetime.now().strftime("%d/%m/%Y")
print(formatted_date)  # 21/11/2024
print(type(formatted_date))  # <class 'str'>

formatted_time = datetime.now().strftime("%H:%M")
print(formatted_time)  # 10:46

# zamiana stringa z datą  na obiekt datatime
data_object = datetime.strptime("21/11/2024", "%d/%m/%Y")
print(data_object)  # 2024-11-21 00:00:00
print(type(data_object))  # <class 'datetime.datetime'>

# tomorrow = today + 1 # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days = 0, seconds = 0, microseconds = 0,
# milliseconds = 0, minutes = 0, hours = 0, weeks = 0)
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2024-11-22

# lista przechowuje
products = [
    {'sku': 1, 'exp_date': today, 'price': 100},
    {'sku': 2, 'exp_date': today, 'price': 200},
    {'sku': 3, 'exp_date': tomorrow, 'price': 300},
    {'sku': 4, 'exp_date': today, 'price': 50},
    {'sku': 5, 'exp_date': today, 'price': 99.99},
]

print(products)
# [{'sku': 1, 'exp_date': datetime.date(2024, 11, 21), 'price': 100},
#  {'sku': 2, 'exp_date': datetime.date(2024, 11, 21), 'price': 200},
#  {'sku': 3, 'exp_date': datetime.date(2024, 11, 22), 'price': 300},
#  {'sku': 4, 'exp_date': datetime.date(2024, 11, 21), 'price': 50},
#  {'sku': 5, 'exp_date': datetime.date(2024, 11, 21), 'price': 99.99}]

for p in products:
    print(p)  # {'sku': 1, 'exp_date': datetime.date(2024, 11, 21), 'price': 100}, słownik
    print(p['exp_date'])  # odczytanie ze słownika daty przydatności 2024-11-21

    if p['exp_date'] != today:
        continue  # zakoncz pętle, weź kolejny element

    p['price'] *= 0.8  # price = price * 0.8
    print(f"""Price for sku {p['sku']}
is now {p['price']}""")
# Price for sku 1
# is now 80.0
# {'sku': 2, 'exp_date': datetime.date(2024, 11, 21), 'price': 200}
# 2024-11-21
# Price for sku 2
# is now 160.0
# {'sku': 3, 'exp_date': datetime.date(2024, 11, 22), 'price': 300}
# 2024-11-22
# {'sku': 4, 'exp_date': datetime.date(2024, 11, 21), 'price': 50}
# 2024-11-21
# Price for sku 4
# is now 40.0
# {'sku': 5, 'exp_date': datetime.date(2024, 11, 21), 'price': 99.99}
# 2024-11-21
# Price for sku 5
# is now 79.992
