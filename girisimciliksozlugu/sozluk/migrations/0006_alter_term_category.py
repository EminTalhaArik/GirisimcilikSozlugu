# Generated by Django 3.2.15 on 2022-10-01 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sozluk', '0005_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sozluk.category'),
        ),
    ]
