from django.db import models


class Item(models.Model):
    name = models.CharField('Название', max_length=150)
    description = models.CharField('Описание', max_length=500)
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.name


class Order(models.Model):
    pass