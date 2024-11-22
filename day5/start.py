# import csv_zad1
#
# print(csv_zad1.products)
import pakiet  # import całego pakietu
from pakiet import fun  # import pliku fun
import pakiet.fun as pk  # import pliku jako alias

fun.powitanie()  # Witam
pk.powitanie()  # Witam
pk.info()
fun.info()
# Jestem pakietem
# Jestem pakietem

# Po dodoaniu w pliku __init__.py
# __all__ = ['info']
#
# from pakiet.fun import info
# import pakietu działa
pakiet.info()  # Jestem pakietem
# pakiet.fun
# Witam
# Witam
# Jestem pakietem
# Jestem pakietem
# Jestem pakietem
