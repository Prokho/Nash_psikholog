# Generated by Django 4.0.4 on 2022-05-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internal_transfer_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.TextField()),
                ('transfer_type', models.IntegerField(choices=[(-1, 'OUT'), (1, 'IN')])),
            ],
        ),
    ]
