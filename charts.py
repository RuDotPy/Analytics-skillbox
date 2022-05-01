import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class AnalyticsCharts:
    def histogram(self, data_column, chart_label, x_label, y_label):
        plt.figure(figsize=(20, 10))
        plt.title(chart_label, fontsize=12)
        plt.xticks(np.arange(0, max(self[data_column]), 1))
        plt.tick_params(labelsize=12)
        sns.histplot(data=self, x=data_column, kde=True)
        plt.show()

    def barplt(self, chart_label):
        plt.figure(figsize=(20, 10))
        plt.title(chart_label, fontsize=12)
        plt.tick_params(labelsize=14)
        sns.barplot(y=self.index, x=self.values, alpha=0.6)
        plt.show()

    def heatmap(self, data_column1, data_column2, chart_label, x_label, y_label):
        sns.jointplot(x=data_column1, y=data_column2, data=self, kind='kde', fill=True,
                      thresh=0, height=8, ratio=7, xlim=[0, 45], ylim=[0, 3200]) \
            .set_axis_labels(x_label, y_label, size=12)
        plt.title(chart_label, fontsize=12)
        plt.show()

    def pie(self, labels, chart_label):
        fig, ax = plt.subplots()
        ax.pie(self, labels=labels)
        ax.set_title(chart_label)
        plt.show()