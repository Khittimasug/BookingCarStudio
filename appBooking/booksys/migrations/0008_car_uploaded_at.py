# Generated by Django 4.2.16 on 2024-10-29 16:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booksys', '0007_remove_car_car_seat_remove_car_car_system_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
