# Generated by Django 5.1.4 on 2025-02-02 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WetCar', '0003_alter_booking_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='WetCar.customer'),
        ),
    ]
