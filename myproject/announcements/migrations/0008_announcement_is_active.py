# Generated by Django 5.1.5 on 2025-06-01 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0007_remove_announcement_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
