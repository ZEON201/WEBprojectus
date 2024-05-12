from django.shortcuts import render, redirect
from .models import Task, CountriesList
from gallery.models import Image
from .forms import TaskForm
from . import cnt


def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def countries_list(request):
    countries = CountriesList.objects.all()
    flags = Image.objects.all()
    return render(request, 'main/elements_list.html', context={"countries": countries, "flags": flags})


def countries_descriptions(request):
    countries = CountriesList.objects.all()
    return render(request, 'main/elements_descriptions.html', context={"countries": countries})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
