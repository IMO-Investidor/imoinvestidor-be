# Generated by Django 5.1.5 on 2025-03-07 20:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('district', '0001_initial'),
        ('municipality', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('street', models.CharField(max_length=510)),
                ('created_by', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_by', models.CharField(blank=True, max_length=255, null=True)),
                ('last_modified_date', models.DateTimeField(blank=True, null=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='district.district')),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='municipality.municipality')),
            ],
        ),
    ]
