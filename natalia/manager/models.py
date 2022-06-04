from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class CustomUser(User):
    phone = models.CharField(max_length=20)
    midlename = models.CharField(max_length=50, null=True, default=None, blank=True)

class Balance(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT)
    balance_value = models.IntegerField(default=0)
    date_last_add = models.DateTimeField(default=None, blank=True, null=True)
    date_last_sub = models.DateTimeField(default=None, blank=True, null=True)

class External_transfer(models.Model):
    TRANSFER_TYPE = ((-1,"OUT"),(1,"IN"))
    balance = models.ForeignKey(Balance, on_delete=models.RESTRICT)
    transfer_value = models.IntegerField(null=False)
    transfer_type = models.IntegerField(null=False, choices=TRANSFER_TYPE)
    transfer_date = models.DateTimeField(default=datetime.now(),null=True)

class Internal_transfer_type(models.Model):
    TRANSFER_TYPE = ((-1,"OUT"),(1,"IN"))
    type_name = models.CharField(max_length=100,null=False)
    transfer_type = models.IntegerField(null=False, choices=TRANSFER_TYPE)

class Internal_transfer(models.Model):
    balance_src = models.ForeignKey(Balance, on_delete=models.RESTRICT, related_name="balance_src")
    balance_dsc = models.ForeignKey(Balance, on_delete=models.RESTRICT, related_name="balance_dsc")
    transfer_value = models.IntegerField(null=False)
    transfer_comission = models.IntegerField(null=False, default=0)
    transfer_date = models.DateTimeField(default=datetime.now(),null=True)
    transfer_type = models.ForeignKey(Internal_transfer_type, on_delete=models.RESTRICT)

class Profile_specialist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT)
    specialist_name = models.TextField(null=False)
    specialist_lastname = models.TextField(null=False)
    specialist_midlename = models.TextField(null=True, blank=True, default=None)
    about = models.TextField(null=False)
    path_photo = models.TextField(null=False)
    url_video = models.TextField(null=False)
    date_confirm_admin = models.DateTimeField(default=None,null=True)
    date_create = models.DateTimeField(default=datetime.now(),null=True)
    actual = models.BooleanField(default=False)

class Service(models.Model):
    service_name = models.TextField(null=False)
    service_description = models.TextField(null=False)

class Profile_service(models.Model):
    profile = models.ForeignKey(Profile_specialist, on_delete=models.RESTRICT)
    service = models.ForeignKey(Service, on_delete=models.RESTRICT)
    price = models.IntegerField(null=False, default=0)

class Specialist_documen(models.Model):
    profile = models.ForeignKey(Profile_specialist, on_delete=models.RESTRICT)
    path_file = models.TextField(null=False)
    show_client = models.BooleanField(default=False)
    description = models.TextField(null=False)
    
class Specialist_photo_type(models.Model):
    poto_type = models.TextField(null=False)

class Specialist_presentation_photo(models.Model):
    profile = models.ForeignKey(Profile_specialist, on_delete=models.RESTRICT)
    path_file = models.TextField(null=False)
    photo_type = models.ForeignKey(Specialist_photo_type, on_delete=models.RESTRICT)
    description = models.TextField(null=False)

class Time_slot(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT)
    date = models.DateField()
    time = models.TimeField()
    create_date = models.DateTimeField()
    remove_date = models.DateTimeField(null=True, blank=True, default=None)
    free = models.BooleanField(blank=True, default=False)

class Appointment(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name="appointment_client")
    specialist = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name="appointment_specialist")
    time_slot = models.ForeignKey(Time_slot, on_delete=models.RESTRICT)
    service = models.ForeignKey(Profile_service, on_delete=models.RESTRICT)
    time_appointment_create = models.DateTimeField(default=datetime.now())
    time_appointment_delete = models.DateTimeField(null=True, blank=True, default=None)
    time_appointment_accept_specialist = models.DateTimeField(null=True, blank=True, default=None)
    description_client = models.TextField(null=True, blank=True, default=None)
    description_specialist = models.TextField(null=True, blank=True, default=None)
    rejection = models.BooleanField(blank=True, default=False)
    
class User_bank_details(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT)
    card_holder = models.TextField()
    card_number = models.IntegerField(null=False)
    card_period = models.TimeField()
    account_number = models.IntegerField(null=False)
    bank_name = models.TextField()
    amount = models.IntegerField(null=False)

class Reason_for_refund(models.Model):
    reason_for_refund = models.TextField(null=False)

class Refusal_or_refund_status(models.Model):
    status =  models.TextField(null=False)
    turn = models.IntegerField(null=False)

class Refund_to_internal_account(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT)
    appointment = models.ForeignKey(Appointment, on_delete=models.RESTRICT)
    reason = models.ForeignKey(Reason_for_refund, on_delete=models.RESTRICT)
    description = models.TextField(null=False)
    status =  models.ForeignKey(Refusal_or_refund_status, on_delete=models.RESTRICT)
    
class Service_cancellation(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.RESTRICT)
    reason = models.ForeignKey(Reason_for_refund, on_delete=models.RESTRICT)
    status =  models.ForeignKey(Refusal_or_refund_status, on_delete=models.RESTRICT)

class Message(models.Model):
    message_from = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name="message_user_from")
    message_to = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name="message_user_to")
    text = models.TextField()
    date_creation = models.DateTimeField(default=datetime.now())
    deletion_date = models.DateTimeField(null=True, blank=True, default=None)
    viewing_date = models.DateTimeField(null=True, blank=True, default=None)
    reply_to = models.ForeignKey('self', on_delete=models.RESTRICT, null=True, blank=True, default=None)

class Message_attachment(models.Model):
    message = models.ForeignKey(Message, on_delete=models.RESTRICT)
    file_link = models.TextField()

class Session(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name="session_client")
    specialist = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name="session_specialist")
    date_creation = models.DateTimeField(default=datetime.now())
    client_confirmation = models.BooleanField(default=False)
    specialist_confirmation = models.BooleanField(default=False)

class Session_feedback(models.Model):
    GRADE = ((1,"ужасно"),(2,""),(3,"нормально"),(4,"хорошо"),(5,"отлично"))
    session = models.ForeignKey(Session, on_delete=models.RESTRICT)
    text = models.TextField()
    date_creation = models.DateTimeField(default=datetime.now())
    deletion_date = models.DateTimeField(null=True, blank=True, default=None)
    grade = models.IntegerField(null=False, choices=GRADE)


class Removed_users(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name="removed_user")
    reason_for_removal = models.TextField()
    who_deleted = models.ForeignKey(CustomUser, on_delete=models.RESTRICT,related_name='who_deleted')


class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name="notification_user")
    text = models.TextField()
    date_creation = models.DateTimeField(default=datetime.now())
    date_sent_to_phone = models.DateTimeField(null=True, blank=True, default=None)
    date_sent_to_email = models.DateTimeField(null=True, blank=True, default=None)












