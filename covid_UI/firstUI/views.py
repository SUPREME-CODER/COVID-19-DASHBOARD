from django.shortcuts import render, HttpResponse
from . import covid_data
# Create your views here.
def analysis(request):
    covid_data_df, covid_data_by_date = covid_data.create_data()
    total_counts = covid_data.total_infected(covid_data_by_date)
    given_date = '2020-06-27'
    type_of_case = 'Confirmed'
    countries, case_counts = covid_data.num_cases_on_a_given_date_country_wise(covid_data_df, given_date, type_of_case, ascending=False, num_countries = 25)
    countries = countries.values.tolist()
    case_counts = case_counts.values.tolist()
    data = {'total_counts':total_counts,
    'countries':countries,
    'case_counts':case_counts,
    'type_of_case':type_of_case,
    'given_date':given_date}
    return render(request, 'firstUI/analysis.html', data)

def about(request):
    return render(request, 'firstUI/developer.html')