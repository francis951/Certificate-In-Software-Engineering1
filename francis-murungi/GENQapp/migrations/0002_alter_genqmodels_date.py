# Generated by Django 4.2 on 2023-04-28 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GENQapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genqmodels',
            name='date',
            field=models.DateField(verbose_name='Date of Birth'),
        ),
    ]