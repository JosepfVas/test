from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='категории')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        if self.description:
            return f'{self.name} {self.description}'
        else:
            return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='продукт')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='product_images/', verbose_name='картинка', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return (f'{self.name} {self.description} {self.price} {self.image} {self.category} {self.price}'
                f'{self.created_at} {self.updated_at}')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукта'
        ordering = ('name',)

