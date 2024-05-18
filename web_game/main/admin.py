from django.contrib import admin
from .models import Task, CountriesList, Answers, QuizSessionInfo


admin.site.register(Task)
admin.site.register(CountriesList)
admin.site.register(Answers)
admin.site.register(QuizSessionInfo)

