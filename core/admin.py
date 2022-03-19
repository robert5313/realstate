from django.contrib import admin

from core.models import Property, Apartment, Expense, RentIncome

class PropertyAdmin(admin.ModelAdmin):
    pass

class ApartmentAdmin(admin.ModelAdmin):
    pass

class ExpenseAdmin(admin.ModelAdmin):
    pass

class RentIncomeAdmin(admin.ModelAdmin):
    pass

# Re-register UserAdmin
admin.site.register(Property, PropertyAdmin)
admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(RentIncome, RentIncomeAdmin)