# Generated by Django 5.0.3 on 2024-04-18 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/product_images/', verbose_name='картинка'),
        ),
    ]