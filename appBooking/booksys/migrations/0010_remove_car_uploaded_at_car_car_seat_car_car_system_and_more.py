# Generated by Django 4.2.16 on 2024-10-29 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksys', '0009_rename_car_picture_car_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='uploaded_at',
        ),
        migrations.AddField(
            model_name='car',
            name='car_seat',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='car_system',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='car_type',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]