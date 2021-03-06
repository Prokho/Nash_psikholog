# Generated by Django 4.0.4 on 2022-05-31 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_appointment_message_profile_specialist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='verify_email',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='verify_phone',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time_appointment_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 23, 31, 16, 498164)),
        ),
        migrations.AlterField(
            model_name='external_transfer',
            name='transfer_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 23, 31, 16, 494175), null=True),
        ),
        migrations.AlterField(
            model_name='internal_transfer',
            name='transfer_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 23, 31, 16, 495172), null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 23, 31, 16, 500158)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 23, 31, 16, 502153)),
        ),
        migrations.AlterField(
            model_name='profile_specialist',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 23, 31, 16, 495172), null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 23, 31, 16, 501156)),
        ),
        migrations.AlterField(
            model_name='session_feedback',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 23, 31, 16, 501156)),
        ),
    ]
