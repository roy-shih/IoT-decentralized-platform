# Generated by Django 3.2.5 on 2021-07-28 06:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_auto_20210728_0627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scene',
            old_name='Device_ID',
            new_name='OpenDevice_ID',
        ),
        migrations.AddField(
            model_name='scene',
            name='closeDevice_ID',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='airconditioner',
            name='Device_ID',
            field=models.CharField(default=uuid.UUID('ac17b05f-9a11-49c6-9549-9e5d033b9a24'), max_length=100),
        ),
        migrations.AlterField(
            model_name='fan',
            name='Device_ID',
            field=models.CharField(default=uuid.UUID('27b8aee7-b708-465c-8b0f-210ed3f2f532'), max_length=100),
        ),
        migrations.AlterField(
            model_name='light',
            name='Device_ID',
            field=models.CharField(default=uuid.UUID('9dde4755-4a50-4a60-85e9-a4edb13ace8b'), max_length=100),
        ),
        migrations.AlterField(
            model_name='other',
            name='Device_ID',
            field=models.CharField(default=uuid.UUID('50f0d22a-7b31-4eba-b1be-74daffe2de2c'), max_length=100),
        ),
    ]