# Generated by Django 5.0.3 on 2024-03-11 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=20)),
                ('name_en', models.CharField(max_length=20)),
                ('name_ru', models.CharField(max_length=20)),
            ],
        ),
    ]