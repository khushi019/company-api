from django.contrib import admin
from .models import *
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','company','position')
    search_fields=('name','position')
    list_filter=('company','position')
    

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')   
    list_filter=('type','location') 

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)