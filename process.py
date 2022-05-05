import csv
import codecs
from tabulate import tabulate
from charts import AnalyticsCharts
import pandas as pd


class AnalyticProcess:
    def __init__(self):
        self.x = None
        self.y = None
        self.dataset_path = None
        self.column_list = []
        self.plot_types = ["barplt", "heatmap", "pie", "histogram"]
        self.plot_type = None
        self.dataset = None

    def set_x(self) -> None:
        self.x = self.column_list[int(input("Укажите индекс колонки: "))]

    def set_y(self) -> None:
        if self.plot_type != "histogram":
            self.y = self.column_list[int(input("Укажите индекс второй колонки: "))]

    def set_dataset(self) -> None:
        self.dataset_path = input("Укажите путь до файла с данными: ")
        self._set_columns_list()
        self.dataset = pd.read_csv(self.dataset_path)

    def get_columns(self) -> None:
        print(tabulate(enumerate(self.column_list), tablefmt="grid"))

    def _set_columns_list(self) -> None:
        if self.dataset_path:
            try:
                with codecs.open(self.dataset_path, "r", "utf_8_sig") as file:
                    csv_reader = csv.reader(file, delimiter=",")
                    for row in csv_reader:
                        self.column_list = row
                        break
            except FileNotFoundError:
                print("Такого файла не существует.")
                self.set_dataset()

    def set_plot_type(self) -> None:
        print(tabulate(enumerate(self.plot_types), tablefmt="grid"))
        self.plot_type = self.plot_types[int(input("Какой тип графика вам нужен? "))]

    def create_plot(self):
        charts = AnalyticsCharts(self.dataset)
        self.get_columns()
        self.set_x()
        self.set_y()
        if self.plot_type == "barplt":
            print("it's barplt")
            charts.barplt(self.x, self.y)
        elif self.plot_type == "heatmap":
            print("it's heatmap")
            charts.heatmap(self.x, self.y, self.x, self.y)
        elif self.plot_type == "pie":
            print("it's pie")
            charts.pie(self.x, self.y)
        elif self.plot_type == "histogram":
            print("it's histogram")
            charts.histogram(self.x)

    def run(self):
        self.set_dataset()
        self.set_plot_type()
        self.create_plot()
