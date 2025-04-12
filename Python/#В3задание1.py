#В3задание1

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Загрузка данных Iris из sklearn
iris = load_iris()
X = iris.data  # Данные
y = iris.target  # Классы (целевая переменная)
feature_names = iris.feature_names # Названия фич
target_names = iris.target_names

# Выбор столбцов (факторные данные)
x_index = 0  # Индекс sepal length
y_index = 1  # Индекс sepal width
x_label = feature_names[x_index]
y_label = feature_names[y_index]

# Цвета для классов
colors = ['purple', 'yellow', 'green']

# Построение диаграммы рассеяния
plt.figure(figsize=(8, 6))  # Создаем фигуру
for label, color in zip(range(len(target_names)), colors):
    plt.scatter(X[y == label, x_index],
                X[y == label, y_index],
                label=target_names[label],
                c=color)

plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title("Iris' Sepal Sizes")
plt.legend()
plt.grid(True)  # Add grid
plt.show()
