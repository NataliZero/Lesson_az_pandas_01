
import pandas as pd

# Загружаем данные из файла dz.csv
df_salary = pd.read_csv('dz.csv')

# Расчет средней зарплаты по каждому городу
average_salary_by_city = df_salary.groupby('City')['Salary'].mean()

print("Средняя зарплата по городам:")
print(average_salary_by_city)
