# Generated by Django 3.2.15 on 2022-10-01 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sozluk', '0003_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
