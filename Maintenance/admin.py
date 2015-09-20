from django.contrib import admin

from Maintenance.models import MaintenanceCategory, MaintenanceItem


admin.site.register(MaintenanceCategory)
admin.site.register(MaintenanceItem)    
