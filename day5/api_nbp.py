import requests

# pip install requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/USD/"

response = requests.get(url)
print(response)
# <Response [200]>
# 200 ok
# 3xx - blędy przekierowania
# 4xx 404 - brak strony, 400 Bad Request - błedy po stronie klienta
# 5xx 500 Internal Server Error - błedy po stronie serwera
print(response.text)
# {"table":"A","currency":"dolar amerykański","code":"USD",
#  "rates":[{"no":"227/A/NBP/2024","effectiveDate":"2024-11-22","mid":4.1752}]}
data = response.json()
print(data)
# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD',
#  'rates': [{'no': '227/A/NBP/2024', 'effectiveDate': '2024-11-22', 'mid': 4.1752}]}
print(data['currency'])  # dolar amerykański
print(data['rates'])
# [
# {'no': '227/A/NBP/2024', 'effectiveDate': '2024-11-22', 'mid': 4.1752}
# ]
print(data['rates'][0]['mid'])  # 4.1752
