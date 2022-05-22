# Generated by Django 4.0.4 on 2022-05-22 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.CharField(max_length=500, verbose_name='Описание')),
                ('price', models.IntegerField(default=0, verbose_name='Цена в центах')),
            ],
        ),
    ]