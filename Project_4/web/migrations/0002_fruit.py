# Generated by Django 4.2.3 on 2023-07-07 16:40

import django.core.validators
from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), web.models.validator_only_letters_in_name])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('nutrition', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
