import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class AnalyticsCharts:

    def __init__(self, data):
        self.data = data

    def histogram(self, data_column):
        fig = plt.figure(figsize=(20, 10))
        plt.xticks(np.arange(0, max(self.data[data_column]), 1))
        plt.tick_params(labelsize=12)
        sns.histplot(data=self.data, x=data_column, kde=True)

        os.makedirs('plots', exist_ok=True)
        fig.savefig('plots/histogram.png')

    def barplt(self, first_column, second_column):
        fig = plt.figure(figsize=(20, 10))
        plt.tick_params(labelsize=14)
        sns.barplot(y=self.data[second_column], x=self.data[first_column], alpha=0.6)

        os.makedirs('plots', exist_ok=True)
        fig.savefig('plots/barplt.png')

    def heatmap(self, data_column1, data_column2, x_label, y_label):
        ax = sns.jointplot(x=data_column1, y=data_column2, data=self.data, kind='kde', fill=True,
                           thresh=0, height=8, ratio=7, xlim=[0, 45], ylim=[0, 3200])
        ax.set_axis_labels(x_label, y_label, size=12)

        os.makedirs('plots', exist_ok=True)
        ax._figure.savefig('plots/heat.png')

    def pie(self, first_column, second_column):
        fig, ax = plt.subplots()
        ax.pie(self.data[first_column], labels=self.data[second_column], textprops={"fontsize": 8})

        os.makedirs('plots', exist_ok=True)
        fig.savefig('plots/pie.png')
