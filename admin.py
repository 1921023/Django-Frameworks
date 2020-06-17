from django.contrib import admin
from .models import Staff, Network
# Register your models here.

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name','designation')

class NetworkAdmin(admin.ModelAdmin):
    list_display = ('summery')
admin.site.register(Staff)
admin.site.register(Network)