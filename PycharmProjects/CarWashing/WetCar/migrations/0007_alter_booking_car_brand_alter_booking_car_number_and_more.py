# Generated by Django 5.1.4 on 2025-02-02 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WetCar', '0006_alter_booking_car_brand_alter_booking_car_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='car_brand',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='car_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
