# Generated by Django 4.2.16 on 2024-10-29 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksys', '0008_car_uploaded_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_picture',
            new_name='file',
        ),
    ]
