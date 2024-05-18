from .models import Task, CountriesList, Answers
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
                   "task": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'})}


# class CountryForm(ModelForm):
#     class Meta:
#         model = CountriesList
#         fields = ["country", "capital", "description"]
#         widgets = {"country": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название страны'}),
#                    "capital": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название столицы'}),
#                    "description": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите описание'})}


class CountryQuiz(ModelForm):
    class Meta:
        model = Answers
        fields = ["answer"]
        widgets = {"answer": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название столицы',
                                              'autocomplete': 'off'})}
