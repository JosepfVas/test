from django.db import models

from main.models import Product


NULLABLE = {'blank': True, 'null': True}


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='version', verbose_name='продукт')
    version_number = models.PositiveIntegerField(verbose_name='номер сорта', unique=True)
    version_name = models.CharField(max_length=50, verbose_name='сорт продукта')
    version_true = models.BooleanField(default=False, verbose_name='текущий сорт')