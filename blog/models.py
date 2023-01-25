from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(blank=True, max_length=150, verbose_name='Назва новини')
    content = models.TextField(blank=True, max_length=5000, verbose_name='Наполенение статьи')
    created_at = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата создания')
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('news_pk', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(blank=True, max_length=150, verbose_name='Название категории')

    def get_absolute_url(self):
        return reverse('news_by_category', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']


class Feedback(models.Model):
    name = models.CharField(blank=True, max_length=50, verbose_name='Имя')
    email = models.CharField(blank=True, max_length=50, verbose_name='Почта')
    phone = models.CharField(blank=True, max_length=30, verbose_name='Телефон')
    content = models.TextField(blank=True, max_length=500, verbose_name='Наполнение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'
        ordering = ['name']
