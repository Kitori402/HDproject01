from django.contrib import admin
from .models import Doctor, Patient, Patient_B, Appointment
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Patient_B)
admin.site.register(Appointment)
