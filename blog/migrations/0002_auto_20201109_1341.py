# Generated by Django 3.1.2 on 2020-11-09 19:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 9, 13, 41, 41, 580170)),
        ),
    ]
