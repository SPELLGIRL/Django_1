# Generated by Django 2.1.5 on 2019-01-31 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-Mail')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес')),
            ],
        ),
        migrations.CreateModel(
            name='CatalogMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Заголовок')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Заголовок')),
                ('link', models.CharField(max_length=200, verbose_name='Ссылка')),
            ],
        ),
        migrations.CreateModel(
            name='NewMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Заголовок')),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='mainapp.Category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('small_img_path', models.ImageField(blank=True, upload_to='product_small_img', verbose_name='Миниатюра')),
                ('big_img_path', models.ImageField(blank=True, upload_to='product_big_img', verbose_name='Изображение')),
                ('category', models.ManyToManyField(blank=True, to='mainapp.Category', verbose_name='Категория')),
            ],
        ),
        migrations.AddField(
            model_name='catalogmenu',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='mainapp.Category', verbose_name='Категория'),
        ),
    ]
