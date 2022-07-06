from django.forms import IntegerField
from .models import *
from django.contrib.auth.models import Group 
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator



def transfer_value_check(value):
        transfer_value = value.get("transfer_value", -1)
        comission = value.get("transfer_comission", -1)
        balance_src = value.get("balance_src")
        balance_dsc = value.get("balance_dsc")
        errors = {}
        if comission < 0 or comission >100:
            errors ["transfer_comission"] = 'Please, input correct value'
        #    raise serializers.ValidationError({"transfer_comission":'Please, input not negative value'})
        
        if transfer_value < 0:
            errors ["transfer_value"] = 'Please, input not negative value'
        #    raise serializers.ValidationError({"transfer_value":'Please, input not negative value'})
        if balance_dsc.id == balance_src.id:
            errors ["balance_src"] ='balance_src should differ balance_dsc'
            errors ["balance_dsc"] ='balance_src should differ balance_dsc'

        if transfer_value > balance_src.balance_value:
            errors ["transfer_value"] = 'transfer value invalid'

        # дз 1 на балансе откуда списываем деньги, деньги есть в нужном количестве
        if balance_src.user.is_active ==False: 
            errors["balance_src"] = 'user was blocked'

        if balance_dsc.user.is_active ==False: 
            errors["balance_dsc"] = 'user was blocked'


        #    errors ["transfer_value"] = 'transfer value invalid'
        # оба пользователя не заблокированы в моей системе
        # 


        if len(errors)>0:
            raise serializers.ValidationError(errors)

        
    

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["name"]

class CustomUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return super().create(validated_data)

    def save(self, validated_data):
        user = self.create(validated_data)
        user.username = user.email
        user.save()
        return user
        
    class Meta:
        model = CustomUser
        fields = ['id','first_name', 'last_name', 'midlename', 'password', 'email', 'phone','verify_email','verify_phone', 'groups']
        read_only_fields = ('id', 'verify_email', 'verify_phone')


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

class Internal_transferSerializer(serializers.ModelSerializer):
    
    def save(self, validated_data):
        balance = self.create(validated_data)
        balance.save()
        return balance

   
    class Meta:
        
        model = Internal_transfer
        fields = "__all__"
        validators = [transfer_value_check]
    

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


