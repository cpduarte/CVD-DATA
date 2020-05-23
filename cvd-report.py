import pandas as pd
covid_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv')
data = covid_data.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()
result = data[data['Confirmed']==data['Deaths']]
result = result[['Country/Region', 'Confirmed', 'Deaths']]
result = result.sort_values('Confirmed', ascending=False)
result = result[result['Confirmed']>0]
result = result.reset_index(drop=True)
print(result)
