from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


# class CountriesList(models.Model):
#
#     country = models.CharField('Название Страны', max_length=50)
#     capital = models.CharField('Столица', max_length=50)
#     description = models.TextField('Описание страны')
#
#     def __str__(self):
#         return self.country

class CountriesList(models.Model):
    id = models.CharField('Id страны', max_length=50, default='null_id', primary_key=True)
    image = models.ImageField(upload_to='images', default='null_flag')
    country = models.CharField('Название Страны', max_length=50)
    capital = models.CharField('Столица', max_length=50)
    description = models.TextField('Описание страны', default='no_description')

    def __str__(self):
        return self.country


class Answers(models.Model):
    answer = models.CharField('Название страны', max_length=50)

    def __str__(self):
        return self.answer


class QuizSessionInfo(models.Model):
    current_question_id = models.CharField('Id текущего вопроса', max_length=50)
    session_score = models.CharField('Количество очков', max_length=50)
    round_counter = models.CharField('Номер раунда', max_length=50, default=1)
    call_from_question_page = models.CharField('Проверка перехода со страницы с вопросом', max_length=50, default=False)

    def __str__(self):
        return self.session_score