from django.db import models


class Item(models.Model):
    """ Товар """
    name = models.CharField('Название', max_length=150)
    description = models.CharField('Описание', max_length=500)
    price = models.IntegerField('Цена в центах')

    def __str__(self):
        return self.name

    class META:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
