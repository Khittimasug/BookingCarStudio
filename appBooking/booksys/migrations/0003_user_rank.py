# Generated by Django 4.2.16 on 2024-10-29 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksys', '0002_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rank',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
