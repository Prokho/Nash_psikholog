from .models import *
from rest_framework import serializers

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'phone', 'email']

class BalanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Balance
        fields = "__all__"

class External_transferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = External_transfer
        fields = "__all__"

class Internal_transfer_typeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Internal_transfer_type
        fields = "__all__"

class Internal_transferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Internal_transfer
        fields = "__all__"

class Profile_specialistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile_specialist
        fields = "__all__"

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class Profile_serviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile_service
        fields = "__all__"

class Specialist_documenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Specialist_documen
        fields = "__all__"

class Specialist_photo_typeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Specialist_photo_type
        fields = "__all__"

class Specialist_presentation_photoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Specialist_presentation_photo
        fields = "__all__"

class Time_slotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Time_slot
        fields = "__all__"

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"

class User_bank_detailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_bank_details
        fields = "__all__"

class Reason_for_refundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reason_for_refund
        fields = "__all__"

class Refusal_or_refund_statusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Refusal_or_refund_status
        fields = "__all__"

class Refund_to_internal_accountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Refund_to_internal_account
        fields = "__all__"

class Service_cancellationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service_cancellation
        fields = "__all__"

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

class Message_attachmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message_attachment
        fields = "__all__"

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"

class Session_feedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session_feedback
        fields = "__all__"

class Removed_usersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Removed_users
        fields = "__all__"

class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


