# Generated by Django 5.0.6 on 2024-06-20 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('course_department', models.CharField(max_length=100)),
                ('course_prerequisites', models.TextField()),
                ('course_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('semester', models.PositiveSmallIntegerField()),
                ('course_head', models.CharField(max_length=30)),
                ('enrollment_limit', models.PositiveIntegerField()),
            ],
        ),
    ]
