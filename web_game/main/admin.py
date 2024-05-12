from django.contrib import admin
from .models import Task, CountriesList


admin.site.register(Task)
admin.site.register(CountriesList)