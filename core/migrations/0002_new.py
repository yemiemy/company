# Generated by Django 4.0.3 on 2023-02-03 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('link', models.URLField(max_length=508)),
                ('created_at', models.DateField(default=datetime.date(2023, 2, 3))),
            ],
        ),
    ]
