from django.contrib import admin
from .models import *


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'device_type', 'active', 'address')
    search_fields = ['address']
    list_filter = ['device_type', 'active']


admin.site.register(CommunicationDevice, DeviceAdmin)
