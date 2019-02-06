# Generated by Django 2.1.5 on 2019-02-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='mainmenu',
            name='link',
            field=models.CharField(max_length=200, unique=True, verbose_name='Ссылка'),
        ),
    ]
