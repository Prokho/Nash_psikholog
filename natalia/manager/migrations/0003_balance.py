# Generated by Django 4.0.4 on 2022-05-03 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_customuser_midlename_alter_customuser_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_value', models.IntegerField(default=0)),
                ('date_last_add', models.DateTimeField(blank=True, default=None, null=True)),
                ('date_last_sub', models.DateTimeField(blank=True, default=None, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.customuser')),
            ],
        ),
    ]