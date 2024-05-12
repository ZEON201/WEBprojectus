from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


# class Elementslist(models.Model):
#
#     country = models.CharField('Название элемента', max_length=50)
#     capital = models.CharField('Столица', max_length=50)
#     description = models.TextField('Описание страны')
#
#     def __str__(self):
#         return self.country

class ElementsList(models.Model):
    image = models.ImageField(upload_to='images', default='null_flag')
    country = models.CharField('Название Страны', max_length=50)
    capital = models.CharField('Столица', max_length=50)
    description = models.TextField('Описание страны', default='no_description')

    def __str__(self):
        return self.country
