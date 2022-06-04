from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Balance)
admin.site.register(Internal_transfer_type)
admin.site.register(Internal_transfer)
admin.site.register(External_transfer)
admin.site.register(Profile_specialist)
admin.site.register(Service)
admin.site.register(Profile_service)
admin.site.register(Specialist_documen)
admin.site.register(Specialist_photo_type)
admin.site.register(Specialist_presentation_photo)
admin.site.register(Time_slot)
admin.site.register(Appointment)
admin.site.register(User_bank_details)
admin.site.register(Reason_for_refund)
admin.site.register(Refusal_or_refund_status)
admin.site.register(Refund_to_internal_account)
admin.site.register(Service_cancellation)
admin.site.register(Message)
admin.site.register(Message_attachment)
admin.site.register(Session)
admin.site.register(Session_feedback)
admin.site.register(Removed_users)
admin.site.register(Notification)

