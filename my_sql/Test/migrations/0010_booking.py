# Generated by Django 5.1 on 2024-10-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0009_alter_uploadedfile_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventTitle', models.CharField(max_length=255)),
                ('startDateTime', models.DateTimeField(blank=True, null=True)),
                ('endDateTime', models.DateTimeField(blank=True, null=True)),
                ('descript', models.TextField(blank=True)),
            ],
        ),
    ]