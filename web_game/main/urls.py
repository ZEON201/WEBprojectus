from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('countries_list', views.countries_list, name='countries_list'),
    path('countries_descriptions', views.countries_descriptions, name='countries_descriptions'),
    path('question', views.get_questions, name='question'),
    path('question/start', views.get_questions, {'is_start': True}, name='question/start'),
    path('question_flags/start', views.get_questions, {'is_start': True, 'is_flags': True}, name='question_flags/start'),
    path('question_flags', views.get_questions, {'is_flags': True}, name='question_flags'),
    path('answer', views.get_answer, name='answer'),
    path('answer_flags', views.get_answer, {'is_flags': True}, name='answer_flags'),
    # path('about', views.about, name='about'),
    # path('create', views.create, name='create'),
    path('finish', views.get_finish, name='finish')
]

