# Generated by Django 3.2.15 on 2022-10-01 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sozluk', '0006_alter_term_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
