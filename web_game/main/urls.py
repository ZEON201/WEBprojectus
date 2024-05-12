from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('countries_list', views.countries_list, name='countries_list'),
    path('countries_descriptions', views.countries_descriptions, name='countries_descriptions'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create')
]

