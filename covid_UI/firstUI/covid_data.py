import pandas as pd
import numpy as np
import matplotlib.pyplot as mp

def create_data():
    confirmed_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    deaths_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
    recovered_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
    urls = [confirmed_url, deaths_url, recovered_url]
    types = ['Confirmed', 'Death', 'Recovered']
    data = []
    for url, type_of_case in zip(urls, types):
        raw_data = pd.read_csv(url)
        melted_data = pd.melt(raw_data,
                              id_vars = ['Province/State', 'Country/Region', 'Lat', 'Long'],
                              var_name = 'Date',
                              value_name = type_of_case)
        data.append(melted_data)
    covid_data = data[0].join(data[1]['Death']).join(data[2]['Recovered'])
    covid_data['Date'] = pd.to_datetime(covid_data['Date'])
    return covid_data, covid_data.groupby('Date').sum()


# covid_data_by_date = covid_data.groupby('Date').sum()

def total_infected(covid_data_by_date):
    return covid_data_by_date.iloc[-1, 2]

def num_cases_on_a_given_date_country_wise(data, given_date, type_of_case, ascending=False, num_countries = 10):
    data_grouped_by_date_and_country = data.groupby(['Date', 'Country/Region']).sum()
    data_on_a_date_country_wise = data_grouped_by_date_and_country.loc[given_date, :]
    
    if ascending:
        data_on_a_date_country_wise = data_on_a_date_country_wise.nsmallest(min(num_countries, len(data_on_a_date_country_wise)), 'Confirmed')
    else:
        data_on_a_date_country_wise = data_on_a_date_country_wise.nlargest(min(num_countries, len(data_on_a_date_country_wise)), 'Confirmed')
    
    data_on_a_date_country_wise = data_on_a_date_country_wise.sort_values(by = type_of_case, ascending=False)
    countries = data_on_a_date_country_wise.reset_index()['Country/Region']
    case_counts = data_on_a_date_country_wise[type_of_case]

    return countries, case_counts

def current_cases(covid_data, json_url = 'https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json'):
    # covid_data_by_country = covid_data.groupby(['Country/Region']).sum()
    dataforMap = []
    map_data = pd.read_json(json_url)
    last_date = covid_data['Date'].iloc[-1]
    last_date_data = covid_data.groupby(['Date', 'Country/Region']).sum().loc[last_date].reset_index()[['Country/Region', 'Confirmed', 'Death', 'Recovered']]
    for i in last_date_data['Country/Region'].unique():
        try:
            tempdf = map_data[map_data['name'] == i]
            temp = {}
            temp['code3'] = list(tempdf['code3'].values)[0]
            temp['name'] = i
            temp['Confirmed'] = last_date_data[last_date_data['Country/Region']==i]['Confirmed'].values[0]
            temp['Death'] = last_date_data[last_date_data['Country/Region']==i]['Death'].values[0]
            temp['Recovered'] = last_date_data[last_date_data['Country/Region']==i]['Recovered'].values[0]
            temp['code'] = list(tempdf['code'].values)[0]
            temp['value'] = temp['Confirmed']
            dataforMap.append(temp)
        except:
            pass
    return dataforMap


def singleCountryData(covid_data, country):
    country_data = covid_data.groupby(['Country/Region', 'Date']).sum().loc[country, ['Confirmed', 'Death', 'Recovered']]
    country_conf = country_data['Confirmed'].values.tolist()
    country_death = country_data['Death'].values.tolist()
    country_recov = country_data['Recovered'].values.tolist()
    dates = country_data.index.tolist()
    return country_conf, country_death, country_recov, dates
