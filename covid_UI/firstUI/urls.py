from django.urls import path
from . import views

urlpatterns = [
    path('analysis/', views.analysis, name = 'analysis-home'),
    path('analysis/singleCountry/', views.countryAnalysis, name = 'analysis-country'),
    path('', views.about, name = 'dev')
]