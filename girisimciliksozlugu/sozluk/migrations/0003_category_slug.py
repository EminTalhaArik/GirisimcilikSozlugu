# Generated by Django 3.2.15 on 2022-10-01 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sozluk', '0002_alter_term_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
