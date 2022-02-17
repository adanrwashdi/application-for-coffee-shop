# Generated by Django 4.0 on 2022-01-22 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('coffee_app', '0003_tabletype_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='booked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='table',
            name='booked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tables_booked', to='auth.user'),
        ),
    ]
