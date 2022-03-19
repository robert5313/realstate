from django.contrib import admin

from management.models import Employee
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton

# class EmployeeInline(admin.StackedInline):
#     model = Employee
#     can_delete = True
#     verbose_name_plural = 'employee'

class EmployeeAdmin(admin.ModelAdmin):
    pass

# Re-register UserAdmin
admin.site.register(Employee, EmployeeAdmin)