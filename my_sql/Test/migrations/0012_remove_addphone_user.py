# Generated by Django 4.2.16 on 2024-10-19 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0011_addphone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addphone',
            name='user',
        ),
    ]