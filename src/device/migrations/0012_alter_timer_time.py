# Generated by Django 3.2.5 on 2021-07-29 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0011_auto_20210729_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='time',
            field=models.TimeField(),
        ),
    ]
