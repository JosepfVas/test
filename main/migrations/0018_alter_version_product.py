# Generated by Django 5.0.3 on 2024-04-29 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_version_version_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='version', to='main.product', verbose_name='продукт'),
        ),
    ]
