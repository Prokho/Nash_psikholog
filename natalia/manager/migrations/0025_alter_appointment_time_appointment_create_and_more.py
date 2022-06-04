# Generated by Django 4.0.4 on 2022-05-21 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0024_alter_appointment_time_appointment_create_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time_appointment_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 21, 14, 28, 44, 554603)),
        ),
        migrations.AlterField(
            model_name='external_transfer',
            name='transfer_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 21, 14, 28, 44, 549603), null=True),
        ),
        migrations.AlterField(
            model_name='internal_transfer',
            name='transfer_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 21, 14, 28, 44, 551605), null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 21, 14, 28, 44, 557603)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 21, 14, 28, 44, 560604)),
        ),
        migrations.AlterField(
            model_name='profile_specialist',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 21, 14, 28, 44, 551605), null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 21, 14, 28, 44, 558604)),
        ),
        migrations.AlterField(
            model_name='session_feedback',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 21, 14, 28, 44, 559604)),
        ),
    ]