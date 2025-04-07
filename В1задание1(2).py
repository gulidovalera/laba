import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

class IrisScatterPlot: #IrisScatterPlot: Создаем класс, который инкапсулирует данные Iris и логику для построения диаграммы рассеяния.
    def __init__(self, x_index=0, y_index=1):
        self.x_index = x_index
        self.y_index = y_index
        self.iris = load_iris()
        self.X = self.iris.data
        self.y = self.iris.target
        self.feature_names = self.iris.feature_names
        self.target_names = self.iris.target_names
        self.colors = ['purple', 'yellow', 'green']

    def plot(self):
        x_label = self.feature_names[self.x_index]
        y_label = self.feature_names[self.y_index]

        plt.figure(figsize=(8, 6))
        for label, color in zip(range(len(self.target_names)), self.colors):
            plt.scatter(self.X[self.y == label, self.x_index],
                        self.X[self.y == label, self.y_index],
                        label=self.target_names[label],
                        c=color)

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title("Iris' Sepal Sizes")
        plt.legend()
        plt.grid(True)
        plt.show()

iris_plot = IrisScatterPlot() # Можно задать индексы столбцов при создании объекта
iris_plot.plot()