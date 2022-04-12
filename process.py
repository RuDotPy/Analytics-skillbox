import csv
import codecs
from tabulate import tabulate


class AnalyticProcess:
    def __init__(self):
        self.x = None
        self.y = None
        self.dataset_path = None
        self.column_list = []

    def set_x(self, value: str) -> None:
        self.x = int(value)

    def set_y(self, value: str) -> None:
        self.y = int(value)

    def set_dataset_path(self) -> None:
        self.dataset_path = input('Укажите путь до файла с данными: ')
        self._set_columns_list()

    def get_columns(self) -> None:
        print(tabulate(enumerate(self.column_list), tablefmt="grid"))

    def _set_columns_list(self) -> None:
        if self.dataset_path:
            try:
                with codecs.open(self.dataset_path, 'r', 'utf_8_sig') as file:
                    csv_reader = csv.reader(file, delimiter=',')
                    for row in csv_reader:
                        self.column_list = row
                        break
            except FileNotFoundError:
                print("Такого файла не существует.")
                self.set_dataset_path()

    def run(self):
        self.set_dataset_path()
        self.get_columns()
