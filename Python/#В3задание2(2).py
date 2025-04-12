#В3задание2(2)
import matplotlib.pyplot as plt
import statsmodels.api as sm

class CO2TimeSeriesPlot:
    def __init__(self, start_date='1958-01-01', end_date='1980-12-31'):
        self.start_date = start_date
        self.end_date = end_date
        self.data = sm.datasets.co2.load_pandas()
        self.co2 = self.data.data
        self.co2_selection = self.co2[self.start_date:self.end_date]

    def plot(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.co2_selection.index, self.co2_selection['co2'], label='CO2 Level')

        plt.xlabel('Date')
        plt.ylabel('CO2 Level (ppm)')
        plt.title(f'CO2 Levels Over Time ({self.start_date} - {self.end_date})')
        plt.legend()
        plt.grid(True)
        plt.show()

# Использование:
co2_plot = CO2TimeSeriesPlot() # Можно задать даты при создании объекта
co2_plot.plot()