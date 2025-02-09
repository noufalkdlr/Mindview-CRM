from django.contrib import admin

from .models import EmployeesDetails

# Register your models here.

class EmployeesDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation',)

admin.site.register(EmployeesDetails, EmployeesDetailsAdmin)
