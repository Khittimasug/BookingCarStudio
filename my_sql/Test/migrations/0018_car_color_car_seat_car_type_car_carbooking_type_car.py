# Generated by Django 4.2.16 on 2024-10-20 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0017_car_carbooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='seat',
            field=models.IntegerField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='type_car',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carbooking',
            name='type_car',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
