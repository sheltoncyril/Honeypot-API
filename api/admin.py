from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, HoneypotTemplate, Honeypot, Trigger

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(HoneypotTemplate)
admin.site.register(Honeypot)
admin.site.register(Trigger)