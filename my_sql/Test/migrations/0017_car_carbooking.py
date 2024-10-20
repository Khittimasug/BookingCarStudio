# Generated by Django 4.2.16 on 2024-10-20 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0016_remove_addphone_user_remove_addphone_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_file', models.ImageField(upload_to='uploads/')),
                ('car_name', models.CharField(max_length=255)),
                ('car_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='carBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=255)),
                ('car_id', models.CharField(max_length=255)),
                ('startDateTime', models.DateTimeField(blank=True, null=True)),
                ('endDateTime', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
