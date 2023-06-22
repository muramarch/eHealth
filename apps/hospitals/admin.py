from django.contrib import admin

from .models import Hospital, Doctor, Review, Appointment

admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Review)
admin.site.register(Appointment)
