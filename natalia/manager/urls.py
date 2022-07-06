from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'group', GroupViewSet)
router.register(r'users', CustomUserViewSet)
router.register(r'balances', BalanceViewSet)
router.register(r'external_transfers', External_transferViewSet)
router.register(r'internal_transfer_types', Internal_transfer_typeViewSet)
router.register(r'internal_transfers', Internal_transferViewSet)
router.register(r'profile_specialists', Profile_specialistViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'profile_services', Profile_serviceViewSet)
router.register(r'specialist_documens', Specialist_documenViewSet)
router.register(r'specialist_photo_types', Specialist_photo_typeViewSet)
router.register(r'specialist_presentation_photos', Specialist_presentation_photoViewSet)
router.register(r'time_slots', Time_slotViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'user_bank_details', User_bank_detailsViewSet)
router.register(r'reason_for_refunds', Reason_for_refundViewSet)
router.register(r'refusal_or_refund_status', Refusal_or_refund_statusViewSet)
router.register(r'refund_to_internal_accounts', Refund_to_internal_accountViewSet)
router.register(r'service_cancellations', Service_cancellationViewSet)
router.register(r'message', MessageViewSet)
router.register(r'message_attachments', Message_attachmentViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'session_feedbacks', Session_feedbackViewSet)
router.register(r'removed_users', Removed_usersViewSet)
router.register(r'notifications', NotificationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]