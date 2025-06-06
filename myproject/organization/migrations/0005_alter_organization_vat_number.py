# Generated by Django 5.1.5 on 2025-04-16 17:49

import organization.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_alter_organization_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='vat_number',
            field=models.CharField(max_length=20, unique=True, validators=[organization.models.validate_portuguese_nif]),
        ),
    ]
