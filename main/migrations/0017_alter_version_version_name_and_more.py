# Generated by Django 5.0.3 on 2024-04-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='version_name',
            field=models.CharField(max_length=50, verbose_name='сорт продукта'),
        ),
        migrations.AlterField(
            model_name='version',
            name='version_number',
            field=models.PositiveIntegerField(unique=True, verbose_name='номер сорта'),
        ),
        migrations.AlterField(
            model_name='version',
            name='version_true',
            field=models.BooleanField(default=False, verbose_name='текущий сорт'),
        ),
    ]
