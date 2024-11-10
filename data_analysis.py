
import pandas as pd

# Загружаем данные из файла об упражнениях
df_exercise = pd.read_csv('Top 50 Excerice for your body.csv')

# Шаг 1: Вывод первых 5 строк
print("Первые 5 строк данных о упражнениях:")
print(df_exercise.head())

# Шаг 2: Информация о данных
print("\nИнформация о данных о упражнениях:")
print(df_exercise.info())

# Шаг 3: Статистическое описание данных
print("\nСтатистическое описание данных:")
print(df_exercise.describe())

# Шаг 4: Среднее количество калорий по уровням сложности
avg_calories_by_difficulty = df_exercise.groupby('Difficulty Level')['Burns Calories (per 30 min)'].mean()
print("\nСреднее количество сжигаемых калорий по уровням сложности:")
print(avg_calories_by_difficulty)
