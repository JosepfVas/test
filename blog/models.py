from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='blog', verbose_name='изображение', **NULLABLE)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    published = models.BooleanField(default=True, verbose_name='публикация')
    views = models.PositiveIntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.title} {self.description} {self.image} {self.created_date} {self.published} {self.views}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

