import pandas as pd

excel_data = pd.read_excel('courses_no_index.xlsx')

print(excel_data)
#   Courses    Fee Duration  Discount
# 0   Spark  25000  50 Days      2000
# 1  Pandas  20000  30 Days      1500
# 2  Python  15000   5 Days       800
# 3     PHP  18000  15 days       500

data = pd.DataFrame(excel_data)
print(data.columns)
# Index(['Courses', 'Fee', 'Duration', 'Discount'], dtype='object')

print(data.index[-1])  # 3
print(data.columns[0])  # Courses, nazwa pierwszej kolumny

pivot_df = pd.pivot_table(data, values='Discount', index="Courses")
print(pivot_df)
#          Discount
# Courses
# PHP         500.0
# Pandas     1500.0
# Python      800.0
# Spark      2000.0
