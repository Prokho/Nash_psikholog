from re import U
from django.forms import IntegerField
from .models import *
from django.contrib.auth.models import Group 
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.core.validators import validate_email




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
        if len(errors)>0:
            raise serializers.ValidationError(errors)

def time_slot_check(value):
        user = value.get("user")
        now_date = datetime.now().date()
        date_1 = value.get("date")
        time_1 = value.get("time")
        date_time_1 = datetime.combine(date_1,time_1)
        dt_prev = date_time_1 - timedelta(hours=1)
        dt_next = date_time_1 + timedelta(hours=1)
        time_prev = dt_prev.time()
        time_next = dt_next.time()
        
        errors = {}

        if user.is_active ==False: 
            errors["user"] = 'user was blocked'
        
        if not user.groups.filter(name__in=['specialist', 'manager']).exists():
            errors["groups"] = 'incorrect role'

        if date_1 < now_date:
            errors["date"] = 'incorrect date, data should be current date or future date'

        if date_1 > (now_date+relativedelta(months=+3)):
            errors["date"] = 'incorrect date,data should be not more than 3 months in future'

        if not time_1.minute %5 == 0:
            errors["time"] = 'incorrect time, time should be devided by 5'

        
        if len(Time_slot.objects.filter(time__gte=time_prev,time__lte=time_next, date=date_1, user=user))!=0:
             errors["time"] = 'incorrect time_slot'

        if len(errors)>0:
            raise serializers.ValidationError(errors)

    
def appointment_check(value):
        client = value.get("client")
        specialist = value.get("specialist")
        time_slot = value.get("time_slot")     
        dt_prev = time_slot.time - timedelta(hours=1)
        dt_next = time_slot.time + timedelta(hours=1)
        

        errors = {}

        if client.is_active ==False: 
            errors["client"] = 'client was blocked'

        if specialist.is_active ==False: 
            errors["specialist"] = 'specialist was blocked'

        if not client.groups.filter(name__in=['client']).exists():
            errors["client"] = 'incorrect role'

        if not specialist.groups.filter(name__in=['specialist']).exists():
            errors["specialist"] = 'incorrect role'

# time_slot сейчас свободен и принадлежит тому же самому психологу (передается ай ди)
        if time_slot.user.id != specialist.id:
            errors["time_slot"] = 'time_slot is held to another specialist'
        elif not time_slot.free_time:
            errors["time_slot"] = 'time_slot is busy'


# time_slot: пользователь не может создать несколько записей на одно и то же дату и время,
#  должны проверяться дата и время для записи клиента
# найти все записи клиента, среди них найти те записи, которые пересекаются с текущим тайм слотом
# из тайм слота нужно вытащить дату и время и на их основе считать пред и след час

        if len(Appointment.objects.filter(time_slot:))!=0:
             errors["time_appointment_create"] = 'incorrect time_appointment' 


        if len(errors)>0:
            raise serializers.ValidationError(errors)


def validate_email_(value):    #!!!
        email = value.get('email')

        errors = {}

        if len(User.email.filter(email=email)) !=0:
            errors["user_email"] = 'email is not unique' 

        if len(errors)>0:
            raise serializers.ValidationError(errors)    




class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]
        
# todo: добавить валидатор  который будет проверять емейл пользователя на уникальность
# примеры валидаторов есть на сайте рест фреймворк
class CustomUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = super().create(validated_data)
        user.username = user.email
        return user

    def save(self, validated_data):
        print(validated_data)
        user = self.create(validated_data)
        user.save()
        balance = Balance.objects.create(user=user)
        balance.save()
        return user

        # при создании пользователя относящегося к группе специалист - создать профайл специалиста и сделать на эту т ему проверку, что создается именно специалист
        
    class Meta:
        model = CustomUser
        fields = ['id','first_name', 'last_name', 'midlename', 'password', 'email', 'phone','verify_email','verify_phone', 'groups']
        read_only_fields = ('id', 'verify_email', 'verify_phone')
        validators = [validate_email_] #!!!



class BalanceSerializer(serializers.ModelSerializer):
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
    

class Profile_specialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile_specialist
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class Profile_serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile_service
        fields = "__all__"

class Specialist_documenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist_documen
        fields = "__all__"
# проверка того, что файл есть на сервере

class Specialist_photo_typeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Specialist_photo_type
        fields = "__all__"

class Specialist_presentation_photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist_presentation_photo
        fields = "__all__"
# проверка того, что файл есть на сервере

class Time_slotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time_slot
        fields = "__all__"
        validators = [time_slot_check, UniqueTogetherValidator(
                queryset=Time_slot.objects.all(),
                fields=['date', 'time', 'user']
            )]

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        validators = [appointment_check]
        
        

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

class Refund_to_internal_accountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund_to_internal_account
        fields = "__all__"

class Service_cancellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_cancellation
        fields = "__all__"

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

class Message_attachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message_attachment
        fields = "__all__"

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"

class Session_feedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session_feedback
        fields = "__all__"

class Removed_usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Removed_users
        fields = "__all__"

class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


