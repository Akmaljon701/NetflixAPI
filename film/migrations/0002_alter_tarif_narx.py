# Generated by Django 4.1.5 on 2023-03-15 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarif',
            name='narx',
            field=models.IntegerField(),
        ),
    ]
