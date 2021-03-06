# Generated by Django 4.0.4 on 2022-05-10 07:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0019_alter_appointment_time_appointment_create_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time_appointment_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 10, 10, 34, 44, 754034)),
        ),
        migrations.AlterField(
            model_name='external_transfer',
            name='transfer_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 10, 10, 34, 44, 745031), null=True),
        ),
        migrations.AlterField(
            model_name='internal_transfer',
            name='transfer_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 10, 10, 34, 44, 746033), null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 10, 10, 34, 44, 760033)),
        ),
        migrations.AlterField(
            model_name='profile_specialist',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 10, 10, 34, 44, 748032), null=True),
        ),
        migrations.CreateModel(
            name='Message_attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_link', models.TextField()),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.message')),
            ],
        ),
    ]
