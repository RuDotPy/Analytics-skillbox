from charts import AnalyticsCharts

import pandas as pd
from datetime import datetime, timedelta
pd.options.mode.chained_assignment = None

df_kiva_loans = pd.read_csv('kiva_loans.csv')

df_loans_dates = df_kiva_loans.dropna(subset=['disbursed_time', 'funded_time'], how='any', inplace=False)
dates = ['posted_time', 'disbursed_time']
df_loans_dates[dates] = df_loans_dates[dates].applymap(lambda x : x.split('+')[0])
df_loans_dates[dates] = df_loans_dates[dates].apply(pd.to_datetime)
df_loans_dates.loc[:, 'time_funding'] = df_loans_dates['disbursed_time']-df_loans_dates['posted_time']
df_loans_dates.loc[:, 'time_funding'] = df_loans_dates['time_funding'] / timedelta(days=1)
dev = (df_loans_dates['time_funding']-df_loans_dates['time_funding'].mean()).abs()
std = df_loans_dates['time_funding'].std()
df_loans_dates_trimmed = df_loans_dates[~(dev > 3 * std) & (df_loans_dates.loc[:, 'time_funding'] > 0)]
df_kiva_loans['borrower_genders'] = [elem if elem in ['female','male'] else 'group' for elem in df_kiva_loans['borrower_genders']]
borrowers = df_kiva_loans['borrower_genders'].value_counts()

data_column1 = 'time_funding'
data_column2 = 'loan_amount'
chart_label = 'Название графика'
x_label = 'Ось X'
y_label = 'Ось Y'

AnalyticsCharts.histogram(df_loans_dates_trimmed, data_column1, chart_label, x_label, y_label)

countries = df_kiva_loans['country'].value_counts()[df_kiva_loans['country'].value_counts(normalize=True) > 0.005]
AnalyticsCharts.barplt(countries, chart_label)

AnalyticsCharts.heatmap(df_loans_dates_trimmed, data_column1, data_column2, chart_label, x_label, y_label)

AnalyticsCharts.pie(countries.values, countries.index, chart_label)