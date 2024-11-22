import pandas

# pip install pandas
# Installing collected packages: pytz, tzdata, six, numpy, python-dateutil, pandas
data = pandas.read_csv('records_dict_list.csv', delimiter=";")

print(data)
# 0    1     today  100.00
# 1    2     today  200.00
# 2    3  tomorrow  300.00
# 3    4     today   50.00
# 4    5     today   99.99

print(data.columns)
# Index(['sku', 'exp_date', 'price'], dtype='object')

print(data.values)
# [[1 'today' 100.0]
#  [2 'today' 200.0]
#  [3 'tomorrow' 300.0]
#  [4 'today' 50.0]
#  [5 'today' 99.99]]
