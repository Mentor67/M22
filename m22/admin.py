from django.contrib import admin
from .models import Machine, MachineStatus, MachineCategory, Provider, ProviderStatus, ProviderType, Part, PartCategory, Maintenance, MaintenanceStatus, MaintenanceType, Material, Labor

# Register your models here.
admin.site.register(Machine)
admin.site.register(MachineStatus)
admin.site.register(MachineCategory)
admin.site.register(Provider)
admin.site.register(ProviderStatus)
admin.site.register(ProviderType)
admin.site.register(Part)
admin.site.register(PartCategory)
admin.site.register(Maintenance)
admin.site.register(MaintenanceStatus)
admin.site.register(MaintenanceType)
admin.site.register(Material)
admin.site.register(Labor)