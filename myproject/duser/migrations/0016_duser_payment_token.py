# Generated by Django 5.1.5 on 2025-06-24 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duser', '0015_duser_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='duser',
            name='payment_token',
            field=models.CharField(default='TFC2025', help_text="Provide payment token or 'unknown' if not available"),
            preserve_default=False,
        ),
    ]
