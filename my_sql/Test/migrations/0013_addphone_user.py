# Generated by Django 4.2.16 on 2024-10-19 21:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Test', '0012_remove_addphone_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='addphone',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='userKey', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
