# Generated by Django 5.1.5 on 2025-06-01 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0006_announcement_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='is_active',
        ),
    ]
