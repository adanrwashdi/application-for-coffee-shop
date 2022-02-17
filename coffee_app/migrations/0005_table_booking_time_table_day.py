# Generated by Django 4.0 on 2022-01-22 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_app', '0004_table_booked_table_booked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='booking_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='table',
            name='day',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]