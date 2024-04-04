import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('covid_data.csv')
df['date'] = pd.to_datetime(df['date'])
df.fillna(0, inplace=True)

total_cases = df['cases'].sum()
total_recoveries = df['recoveries'].sum()
total_deaths = df['deaths'].sum()

us_data = df[df['country'] == 'United States']
us_total_cases = us_data['cases'].sum()
us_total_recoveries = us_data['recoveries'].sum()
us_total_deaths = us_data['deaths'].sum()

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='date', y='cases', label='Cases')
sns.lineplot(data=df, x='date', y='recoveries', label='Recoveries')
sns.lineplot(data=df, x='date', y='deaths', label='Deaths')
plt.title('Global COVID-19 Trends')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(data=us_data, x='date', y='cases', label='Cases')
sns.lineplot(data=us_data, x='date', y='recoveries', label='Recoveries')
sns.lineplot(data=us_data, x='date', y='deaths', label='Deaths')
plt.title('COVID-19 Trends in the United States')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.show()
