from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
#from rest_framework import permissions
from .migrations import *
from .serializers import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all() # автоматическое формирование ответа на get запрос
    serializer_class = CustomUserSerializer

    def create(self, request):
        request = request.data # получаем данные отправленные пользователем
        data = self.serializer_class(data=request) # мы с помощью сериалайзера преобразуем данные из строки в объект
        if data.is_valid():
            user = data.save(data.validated_data) #сохраняем данные в базу данных после проверки
            serializer  = self.serializer_class(user) #сериализуем данные полученные от клиента
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(data.errors, status=400)
        

class BalanceViewSet(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
    http_method_names = ['get']

class External_transferViewSet(viewsets.ModelViewSet):
    queryset = External_transfer.objects.all()
    serializer_class = External_transferSerializer
    http_method_names = ['get']

class Internal_transfer_typeViewSet(viewsets.ModelViewSet):
    queryset = Internal_transfer_type.objects.all()
    serializer_class = Internal_transfer_typeSerializer
    http_method_names = ['get']

class Internal_transferViewSet(viewsets.ModelViewSet):
    queryset = Internal_transfer.objects.all()
    serializer_class = Internal_transferSerializer
    http_method_names = ['get', 'post']

    def create(self, request):
        data = request.data # получаем данные отправленные пользователем
        data = self.serializer_class(data=data) # мы с помощью сериалайзера преобразуем данные из строки в объект
        if data.is_valid():
            data_value = data.save(data.validated_data) #сохраняем данные в базу данных после проверки
            serializer  = self.serializer_class(data_value) #сериализуем данные полученные от клиента
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(data.errors, status=400)           
  

class Profile_specialistViewSet(viewsets.ModelViewSet):
    queryset = Profile_specialist.objects.all()
    serializer_class = Profile_specialistSerializer
    http_method_names = ['get', 'post','update']#?

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    http_method_names = ['get']

class Profile_serviceViewSet(viewsets.ModelViewSet):
    queryset = Profile_service.objects.all()
    serializer_class = Profile_serviceSerializer
    http_method_names = ['get', 'post']


class Specialist_documenViewSet(viewsets.ModelViewSet):
    queryset = Specialist_documen.objects.all()
    serializer_class = Specialist_documenSerializer
    http_method_names = ['get', 'post', 'delete']

class Specialist_photo_typeViewSet(viewsets.ModelViewSet):
    queryset = Specialist_photo_type.objects.all()
    serializer_class = Specialist_photo_typeSerializer
    http_method_names = ['get', 'post', 'delete']


class Specialist_presentation_photoViewSet(viewsets.ModelViewSet):
    queryset = Specialist_presentation_photo.objects.all()
    serializer_class = Specialist_presentation_photoSerializer
    http_method_names = ['get', 'post', 'delete']

class Time_slotViewSet(viewsets.ModelViewSet):
    queryset = Time_slot.objects.all()
    serializer_class = Time_slotSerializer
    http_method_names = ['get', 'post', 'delete']

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class User_bank_detailsViewSet(viewsets.ModelViewSet):
    queryset = User_bank_details.objects.all()
    serializer_class = User_bank_detailsSerializer
    http_method_names = ['get', 'update', 'delete']

class Reason_for_refundViewSet(viewsets.ModelViewSet):
    queryset = Reason_for_refund.objects.all()
    serializer_class = Reason_for_refundSerializer
    http_method_names = ['get']

class Refusal_or_refund_statusViewSet(viewsets.ModelViewSet):
    queryset = Refusal_or_refund_status.objects.all()
    serializer_class = Refusal_or_refund_statusSerializer
    http_method_names = ['get']

class Refund_to_internal_accountViewSet(viewsets.ModelViewSet):
    queryset = Refund_to_internal_account.objects.all()
    serializer_class = Refund_to_internal_accountSerializer
    http_method_names = ['get', 'post', 'delete']

class Service_cancellationViewSet(viewsets.ModelViewSet):
    queryset = Service_cancellation.objects.all()
    serializer_class = Service_cancellationSerializer
    http_method_names = ['get', 'post', 'delete']

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ['get', 'post', 'delete']

class Message_attachmentViewSet(viewsets.ModelViewSet):
    queryset = Message_attachment.objects.all()
    serializer_class = Message_attachmentSerializer
    http_method_names = ['get', 'post']

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    http_method_names = ['get', 'post']

class Session_feedbackViewSet(viewsets.ModelViewSet):
    queryset = Session_feedback.objects.all()
    serializer_class = Session_feedbackSerializer
    http_method_names = ['get', 'post', 'delete']

class Removed_usersViewSet(viewsets.ModelViewSet):
    queryset = Removed_users.objects.all()
    serializer_class = Removed_usersSerializer
    http_method_names = ['get', 'post', 'delete']

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    http_method_names = ['get']

@csrf_exempt
@require_http_methods(["POST"])
def uploadFile(request):
    form = FormUploadFile(request.POST, request.FILES)
    if form.is_valid():
        file = request.FILES["file"]
        