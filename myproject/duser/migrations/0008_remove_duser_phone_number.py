# Generated by Django 5.1.5 on 2025-04-18 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duser', '0007_merge_20250418_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duser',
            name='phone_number',
        ),
    ]
