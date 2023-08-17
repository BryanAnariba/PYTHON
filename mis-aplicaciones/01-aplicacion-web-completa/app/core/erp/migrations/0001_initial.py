# Generated by Django 4.2.4 on 2023-08-16 14:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Register Date')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('age', models.PositiveIntegerField(default=0)),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('status', models.BooleanField(default=True)),
                ('avatar', models.ImageField(upload_to='avatar/%Y/%m/%d')),
                ('curriculum_vitae', models.ImageField(upload_to='curriculum_vitae/%Y/%m/%d')),
                ('gender', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'db_table': 'Employee',
                'ordering': ['id'],
            },
        ),
    ]
