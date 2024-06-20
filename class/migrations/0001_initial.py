# Generated by Django 5.0.6 on 2024-06-20 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('class_name', models.CharField(max_length=20)),
                ('class_description', models.TextField()),
                ('school_year', models.IntegerField()),
                ('capacity', models.PositiveIntegerField()),
                ('room_number', models.PositiveIntegerField()),
                ('grade_level', models.IntegerField()),
                ('class_best_subject', models.CharField(max_length=30)),
                ('class_specialty', models.CharField(max_length=30)),
            ],
        ),
    ]
