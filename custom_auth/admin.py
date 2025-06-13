from django.contrib import admin
from .models import Contact, MembershipPlan, Enrollment, Trainer, Attendance
# Remove "custom_authapp" from the import since we're using relative import
# Register your models here.
admin.site.register(Contact)
admin.site.register(MembershipPlan)
admin.site.register(Enrollment)
admin.site.register(Trainer)
admin.site.register(Attendance)
