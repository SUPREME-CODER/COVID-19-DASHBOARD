from django.shortcuts import render, HttpResponse
from . import covid_data
from pprint import pprint

covid_data_df, covid_data_by_date = covid_data.create_data()

# Create your views here.
def analysis(request):
    total_counts = covid_data.total_infected(covid_data_by_date)
    given_date = '2020-06-27'
    type_of_case = 'Confirmed'
    countries, case_counts = covid_data.num_cases_on_a_given_date_country_wise(covid_data_df, given_date, type_of_case, ascending=False, num_countries = 20)
    countries = countries.values.tolist()
    case_counts = case_counts.values.tolist()
    dataforMap = covid_data.current_cases(covid_data_df)
    mapdata = 'True'

    data = {'total_counts':total_counts,
    'countries':countries,
    'case_counts':case_counts,
    'type_of_case':type_of_case,
    'given_date':given_date,
    'dataforMap':dataforMap,
    'mapdata':mapdata}

    return render(request, 'firstUI/analysis.html', data)

def countryAnalysis(request):
    selectedcountry = request.POST.get('country')
    print('Country:-', selectedcountry)
    total_counts = covid_data.total_infected(covid_data_by_date)
    given_date = '2020-06-27'
    type_of_case = 'Confirmed'
    countries, case_counts = covid_data.num_cases_on_a_given_date_country_wise(covid_data_df, given_date, type_of_case, ascending=False, num_countries = 20)
    countries = countries.values.tolist()
    case_counts = case_counts.values.tolist()
    country_conf, country_death, country_recov, dates = covid_data.singleCountryData(covid_data_df, selectedcountry)
    print('Data', selectedcountry)
    mapdata = 'False'
    
    datasetsForLine = [{'yAxisID': 'y-axis-1','label':'Confirmed Cases','data':country_conf,'borderColor':'#03a9fc','backgroundColor':'#03a9fc','fill':'false'},
                    {'yAxisID': 'y-axis-1','label':'Death Cases','data':country_death,'borderColor':'#fc5203','backgroundColor':'#fc5203','fill':'false'}]
    axisvalues = dates

    data = {'total_counts':total_counts,
    'countries':countries,
    'case_counts':case_counts,
    'type_of_case':type_of_case,
    'given_date':given_date,
    'selectedcountry':selectedcountry,
    'datasetsForLine':datasetsForLine,
    'axisvalues':axisvalues,
    'mapdata':mapdata}

    return render(request, 'firstUI/singleCountry.html', data)




def about(request):
    return render(request, 'firstUI/developer.html')