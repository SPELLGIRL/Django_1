from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Категория')

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    small_img_path = models.ImageField(
        upload_to='product_small_img',
        verbose_name='Миниатюра',
        blank=True
    )
    big_img_path = models.ImageField(
        upload_to='product_big_img',
        verbose_name='Изображение',
        blank=True
    )

    category = models.ManyToManyField(
        Category,
        blank=True,
        verbose_name='Категория'
    )

    def __str__(self):
        return self.title
