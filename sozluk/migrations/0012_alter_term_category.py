# Generated by Django 3.2.9 on 2023-03-23 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sozluk', '0011_auto_20230323_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='category',
            field=models.ManyToManyField(to='sozluk.Category'),
        ),
    ]