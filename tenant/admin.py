from django.contrib import admin

from tenant.models import Tenant
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton

class TenantAdmin(admin.ModelAdmin):
    pass

# Re-register UserAdmin
admin.site.register(Tenant, TenantAdmin)