# Generated by Django 3.2.9 on 2023-03-23 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sozluk', '0007_term_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='term',
            name='category',
        ),
        migrations.AddField(
            model_name='term',
            name='category',
            field=models.ManyToManyField(null=True, to='sozluk.Category'),
        ),
    ]
