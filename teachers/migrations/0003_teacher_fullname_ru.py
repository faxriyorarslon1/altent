# Generated by Django 3.2.11 on 2022-01-29 11:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_rename_yordam_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='fullname_ru',
            field=models.CharField(default="ism yoq", max_length=30),
            preserve_default=False,
        ),
    ]
