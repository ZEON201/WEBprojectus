from django.db import models

# Create your models here.
class Image(models.Model):

    title = models.CharField('Флаг Страны', max_length=50)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
