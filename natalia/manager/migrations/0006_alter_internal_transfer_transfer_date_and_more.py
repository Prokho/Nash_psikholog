# Generated by Django 4.0.4 on 2022-05-08 16:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_alter_internal_transfer_type_type_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internal_transfer',
            name='transfer_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 8, 19, 38, 52, 343024), null=True),
        ),
        migrations.CreateModel(
            name='External_transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_value', models.IntegerField()),
                ('transfer_type', models.IntegerField(choices=[(-1, 'OUT'), (1, 'IN')])),
                ('transfer_date', models.DateTimeField(default=datetime.datetime(2022, 5, 8, 19, 38, 52, 342024), null=True)),
                ('balance', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.balance')),
            ],
        ),
    ]