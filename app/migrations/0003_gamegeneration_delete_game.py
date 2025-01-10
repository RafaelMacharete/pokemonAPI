# Generated by Django 5.1.4 on 2025-01-10 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_ginasy_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameGeneration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abilities', models.TextField()),
                ('names', models.TextField()),
                ('main_region', models.TextField()),
                ('moves', models.CharField(max_length=25)),
                ('pokemon_species', models.CharField(max_length=25)),
                ('types', models.CharField(max_length=25)),
                ('version_groups', models.CharField(max_length=50)),
                ('created', models.DateField(auto_now=True)),
                ('ginasy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ginasy', verbose_name="Pokemon's Ginasy")),
            ],
        ),
        migrations.DeleteModel(
            name='Game',
        ),
    ]
