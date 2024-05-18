from django.shortcuts import render, redirect
import random
from .models import Task, CountriesList, Answers, QuizSessionInfo
from .forms import CountryQuiz


def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def countries_list(request):
    countries = CountriesList.objects.all()
    return render(request, 'main/countries_list.html', context={"countries": countries, })


def countries_descriptions(request):
    countries = CountriesList.objects.all()
    return render(request, 'main/countries_descriptions.html', context={"countries": countries})


def get_questions(request, is_flags=False, is_start=False):
    if is_start:
        request = _reset_quiz(request)
        question = get_next_question(request)
        round = QuizSessionInfo.objects.values('round_counter').first()
        QuizSessionInfo.objects.values('call_from_question_page').update(
            call_from_question_page=True)
    else:
        QuizSessionInfo.objects.values('call_from_question_page').update(
            call_from_question_page=True)
        question = get_next_question(request)
        round = QuizSessionInfo.objects.values('round_counter').first()
        if int(round['round_counter']) > 10:
            return get_finish(request)
    form = CountryQuiz(request.POST)
    # if form.is_valid():
    #     form.save()
    #     return redirect('answer')
    # context = {'question': question, 'form': form, 'round': round['round_counter']}
    if is_flags:
        if form.is_valid():
            form.save()
            return redirect('answer_flags')
        context = {'question': question, 'form': form, 'round': round['round_counter']}
        return render(request, 'main/question_flags.html', context)
    else:
        if form.is_valid():
            form.save()
            return redirect('answer')
        context = {'question': question, 'form': form, 'round': round['round_counter']}
        return render(request, 'main/question.html', context)


def get_answer(request, is_flags=False, is_correct=False):
    if QuizSessionInfo.objects.values('call_from_question_page').first()['call_from_question_page'] == 'True':
        correct_answer_id = QuizSessionInfo.objects.values('current_question_id').first()['current_question_id']
        user_answer = Answers.objects.order_by('id').last()
        if is_flags:
            correct_answer = CountriesList.objects.values('country').get(pk=correct_answer_id)
            if str(user_answer) == str(correct_answer['country']):
                increase_score(request)
                is_correct = True
        else:
            correct_answer = CountriesList.objects.values('capital').get(pk=correct_answer_id)
            if str(user_answer) == str(correct_answer['capital']):
                increase_score(request)
                is_correct = True
        change_question_id(request)
        increase_round(request)
        score = QuizSessionInfo.objects.first()
    else:
        if is_flags:
            return redirect('question_flags')
        else:
            return redirect('question')
    QuizSessionInfo.objects.values('call_from_question_page').update(call_from_question_page=False)
    if is_flags:
        return render(request, 'main/answer_flags.html', context={'user_answer': user_answer,
                                                                  'correct_answer': correct_answer['country'],
                                                                  'is_correct': is_correct, 'score': score})
    else:
        return render(request, 'main/answer.html', context={'user_answer': user_answer,
                                                            'correct_answer': correct_answer['capital'],
                                                            'is_correct': is_correct, 'score': score})


def increase_score(request):
    previous_score = QuizSessionInfo.objects.values('session_score').first()
    print(previous_score['session_score'])
    QuizSessionInfo.objects.values('session_score').update(session_score=int(previous_score['session_score']) + 1)


def increase_round(request):
    previous_round = QuizSessionInfo.objects.values('round_counter').first()
    print(previous_round)
    QuizSessionInfo.objects.values('round_counter').update(round_counter=int(previous_round['round_counter']) + 1)


def change_question_id(request):
    QuizSessionInfo.objects.values('current_question_id').update(
        current_question_id=random.randint(4, 49))


def get_next_question(request):
    current_id = int(QuizSessionInfo.objects.values('current_question_id').first()['current_question_id'])
    return CountriesList.objects.get(pk=current_id)


def get_finish(request):
    score = QuizSessionInfo.objects.values('session_score').first()['session_score']
    return render(request, 'main/finish.html', context={'score': score, 'score_percent': int(score) * 10})


def _reset_quiz(request):
    # QuizSessionInfo.objects.values('current_question_id').update(current_question_id=random.randint(4, 49))
    QuizSessionInfo.objects.values('session_score').update(session_score=0)
    QuizSessionInfo.objects.values('round_counter').update(round_counter=1)
    Answers.objects.all().delete()
    return request
