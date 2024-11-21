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
