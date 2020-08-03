from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
from . import covid_data

# Create your views here.
covid_data_df, covid_data_by_date = covid_data.create_data()
countries, case_counts = covid_data.num_cases_on_a_given_date_country_wise(covid_data_df, type_of_case='Confirmed', ascending=False, num_countries = 188)
total_count = covid_data.total_infected(covid_data_by_date)
df3=pd.read_json('https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')

def index(request):
    dataForMap = covid_data.current_cases(covid_data_df)

    data = {'countries':countries,
        'case_counts':case_counts,
        'total_count':total_count,
        'dataForMap':dataForMap,
        'maxVal':max(case_counts)}

    return render(request,'index.html',data)


def drillDownACountry(request):
    print(request.POST.dict())
    countryName=request.POST.get('countryName')

    country_conf, country_death, country_recov, dates = covid_data.singleCountryData(covid_data_df, countryName)

    datasetsForLine=[{'yAxisID': 'y-axis-1','label':'Daily Confirmed Cases','data':country_conf,'borderColor':'#8000FF','backgroundColor':'#8000FF','fill':'false'},
                    {'yAxisID': 'y-axis-2','label':'Daily Death Cases','data':country_death,'borderColor':'#fc5203','backgroundColor':'#fc5203','fill':'false'}]
    axisvalues=list(range(1, len(dates) + 1))

    data = {'countryName':countryName,
        'countries':countries,
        'case_counts':case_counts,
        'total_count':total_count,
        'datasetsForLine':datasetsForLine,
        'axisvalues':axisvalues,
        'maxVal':max(case_counts)}

    return render(request,'index2.html',data)

