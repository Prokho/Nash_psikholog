from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
#from rest_framework import permissions
from .migrations import *
from .serializers import *


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class BalanceViewSet(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer

class External_transferViewSet(viewsets.ModelViewSet):
    queryset = External_transfer.objects.all()
    serializer_class = External_transferSerializer


class Internal_transfer_typeViewSet(viewsets.ModelViewSet):
    queryset = Internal_transfer_type.objects.all()
    serializer_class = Internal_transfer_typeSerializer

class Internal_transferViewSet(viewsets.ModelViewSet):
    queryset = Internal_transfer.objects.all()
    serializer_class = Internal_transferSerializer

class Profile_specialistViewSet(viewsets.ModelViewSet):
    queryset = Profile_specialist.objects.all()
    serializer_class = Profile_specialistSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class Profile_serviceViewSet(viewsets.ModelViewSet):
    queryset = Profile_service.objects.all()
    serializer_class = Profile_serviceSerializer

class Specialist_documenViewSet(viewsets.ModelViewSet):
    queryset = Specialist_documen.objects.all()
    serializer_class = Specialist_documenSerializer

class Specialist_photo_typeViewSet(viewsets.ModelViewSet):
    queryset = Specialist_photo_type.objects.all()
    serializer_class = Specialist_photo_typeSerializer

class Specialist_photo_typeViewSet(viewsets.ModelViewSet):
    queryset = Specialist_photo_type.objects.all()
    serializer_class = Specialist_photo_typeSerializer

class Specialist_presentation_photoViewSet(viewsets.ModelViewSet):
    queryset = Specialist_presentation_photo.objects.all()
    serializer_class = Specialist_presentation_photo

class Time_slotViewSet(viewsets.ModelViewSet):
    queryset = Time_slot.objects.all()
    serializer_class = Time_slotSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class User_bank_detailsViewSet(viewsets.ModelViewSet):
    queryset = User_bank_details.objects.all()
    serializer_class = User_bank_detailsSerializer

class Reason_for_refundViewSet(viewsets.ModelViewSet):
    queryset = Reason_for_refund.objects.all()
    serializer_class = Reason_for_refundSerializer

class Refusal_or_refund_statusViewSet(viewsets.ModelViewSet):
    queryset = Refusal_or_refund_status.objects.all()
    serializer_class = Refusal_or_refund_statusSerializer

class Refund_to_internal_accountViewSet(viewsets.ModelViewSet):
    queryset = Refund_to_internal_account.objects.all()
    serializer_class = Refund_to_internal_accountSerializer

class Service_cancellationViewSet(viewsets.ModelViewSet):
    queryset = Service_cancellation.objects.all()
    serializer_class = Service_cancellationSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class Message_attachmentViewSet(viewsets.ModelViewSet):
    queryset = Message_attachment.objects.all()
    serializer_class = Message_attachmentSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class Session_feedbackViewSet(viewsets.ModelViewSet):
    queryset = Session_feedback.objects.all()
    serializer_class = Session_feedbackSerializer

class Removed_usersViewSet(viewsets.ModelViewSet):
    queryset = Removed_users.objects.all()
    serializer_class = Removed_usersSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

