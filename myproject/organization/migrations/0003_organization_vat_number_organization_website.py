# Generated by Django 5.1.5 on 2025-03-18 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_alter_organization_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='vat_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
