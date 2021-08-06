from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Ticket(models.Model):
    title = models.CharField(max_length=150, verbose_name='Тема')
    content = models.TimeField(blank=True, verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    state = models.ForeignKey('State', on_delete=models.PROTECT, verbose_name='Состояние')
    priority = models.ForeignKey('Priority', on_delete=models.PROTECT, verbose_name='Приоритет')
    assigned = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Исполнитель')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['created_at']


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class State(models.Model):
    title = models.CharField(max_length=50, verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ['title']


class Priority(models.Model):
    title = models.CharField(max_length=50, verbose_name='Приоритет')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Приоритет'
        verbose_name_plural = 'Приоритеты'
        ordering = ['title']
