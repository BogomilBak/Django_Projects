# Generated by Django 4.2.3 on 2023-07-05 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.CharField(choices=[('Sports Car', 'Sports Car'), ('Pickup', 'Pickup'), ('Crossover', 'Crossover'), ('Minibus', 'Minibus'), ('Other', 'Other')], max_length=10, verbose_name='Type'),
        ),
    ]
