# Generated by Django 4.0.4 on 2022-07-07 16:43

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_appointment_create', models.DateTimeField(default=datetime.datetime(2022, 7, 7, 19, 43, 52, 858665))),
                ('time_appointment_delete', models.DateTimeField(blank=True, default=None, null=True)),
                ('time_appointment_accept_specialist', models.DateTimeField(blank=True, default=None, null=True)),
                ('description_client', models.TextField(blank=True, default=None, null=True)),
                ('description_specialist', models.TextField(blank=True, default=None, null=True)),
                ('rejection', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_value', models.IntegerField(default=0)),
                ('date_last_add', models.DateTimeField(blank=True, default=None, null=True)),
                ('date_last_sub', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=20)),
                ('midlename', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('verify_email', models.BooleanField(blank=True, default=False)),
                ('verify_phone', models.BooleanField(blank=True, default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Internal_transfer_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100)),
                ('transfer_type', models.IntegerField(choices=[(-1, 'OUT'), (1, 'IN')])),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_creation', models.DateTimeField(default=datetime.datetime(2022, 7, 7, 19, 43, 52, 863664))),
                ('deletion_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('viewing_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('message_from', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='message_user_from', to='manager.customuser')),
                ('message_to', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='message_user_to', to='manager.customuser')),
                ('reply_to', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='manager.message')),
            ],
        ),
        migrations.CreateModel(
            name='Profile_specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialist_name', models.TextField()),
                ('specialist_lastname', models.TextField()),
                ('specialist_midlename', models.TextField(blank=True, default=None, null=True)),
                ('about', models.TextField()),
                ('path_photo', models.TextField()),
                ('url_video', models.TextField()),
                ('date_confirm_admin', models.DateTimeField(default=None, null=True)),
                ('date_create', models.DateTimeField(default=datetime.datetime(2022, 7, 7, 19, 43, 52, 855664), null=True)),
                ('actual', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Reason_for_refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_for_refund', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Refusal_or_refund_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField()),
                ('turn', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.TextField()),
                ('service_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(default=datetime.datetime(2022, 7, 7, 19, 43, 52, 864666))),
                ('client_confirmation', models.BooleanField(default=False)),
                ('specialist_confirmation', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='session_client', to='manager.customuser')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='session_specialist', to='manager.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Specialist_photo_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poto_type', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User_bank_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_holder', models.TextField()),
                ('card_number', models.IntegerField()),
                ('card_period', models.TimeField()),
                ('account_number', models.IntegerField()),
                ('bank_name', models.TextField()),
                ('amount', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Time_slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('create_date', models.DateTimeField()),
                ('remove_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('free_time', models.BooleanField(blank=True, default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Specialist_presentation_photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_file', models.TextField()),
                ('description', models.TextField()),
                ('photo_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.specialist_photo_type')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.profile_specialist')),
            ],
        ),
        migrations.CreateModel(
            name='Specialist_documen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_file', models.TextField()),
                ('show_client', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.profile_specialist')),
            ],
        ),
        migrations.CreateModel(
            name='Session_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_creation', models.DateTimeField(default=datetime.datetime(2022, 7, 7, 19, 43, 52, 864666))),
                ('deletion_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('grade', models.IntegerField(choices=[(1, 'ужасно'), (2, ''), (3, 'нормально'), (4, 'хорошо'), (5, 'отлично')])),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.session')),
            ],
        ),
        migrations.CreateModel(
            name='Service_cancellation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.customuser')),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.reason_for_refund')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.refusal_or_refund_status')),
            ],
        ),
        migrations.CreateModel(
            name='Removed_users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_for_removal', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='removed_user', to='manager.customuser')),
                ('who_deleted', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='who_deleted', to='manager.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Refund_to_internal_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.appointment')),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.reason_for_refund')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.refusal_or_refund_status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Profile_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.profile_specialist')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.service')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_creation', models.DateTimeField(default=datetime.datetime(2022, 7, 7, 19, 43, 52, 865665))),
                ('date_sent_to_phone', models.DateTimeField(blank=True, default=None, null=True)),
                ('date_sent_to_email', models.DateTimeField(blank=True, default=None, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='notification_user', to='manager.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Message_attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_link', models.TextField()),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.message')),
            ],
        ),
        migrations.CreateModel(
            name='Internal_transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_value', models.IntegerField()),
                ('transfer_comission', models.IntegerField(default=0)),
                ('transfer_date', models.DateTimeField(default=datetime.datetime(2022, 7, 7, 19, 43, 52, 854663), null=True)),
                ('balance_dsc', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='balance_dsc', to='manager.balance')),
                ('balance_src', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='balance_src', to='manager.balance')),
                ('transfer_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.internal_transfer_type')),
            ],
        ),
        migrations.CreateModel(
            name='External_transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_value', models.IntegerField()),
                ('transfer_type', models.IntegerField(choices=[(-1, 'OUT'), (1, 'IN')])),
                ('transfer_date', models.DateTimeField(default=datetime.datetime(2022, 7, 7, 19, 43, 52, 853664), null=True)),
                ('balance', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.balance')),
            ],
        ),
        migrations.AddField(
            model_name='balance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.customuser'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='appointment_client', to='manager.customuser'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.profile_service'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='specialist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='appointment_specialist', to='manager.customuser'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='time_slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='manager.time_slot'),
        ),
    ]
