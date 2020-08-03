from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.analysis, name = 'analysis-home'),
    path(r'singleCountry/', views.countryAnalysis, name = 'analysis-country'),
    # path('', views.about, name = 'dev')
]