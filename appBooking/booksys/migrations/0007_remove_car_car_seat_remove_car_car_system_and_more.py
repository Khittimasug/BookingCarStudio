# Generated by Django 4.2.16 on 2024-10-29 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksys', '0006_alter_car_car_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_seat',
        ),
        migrations.RemoveField(
            model_name='car',
            name='car_system',
        ),
        migrations.RemoveField(
            model_name='car',
            name='car_type',
        ),
    ]
