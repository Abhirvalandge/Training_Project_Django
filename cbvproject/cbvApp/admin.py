from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db import models
from .models import Employee

# Register your models here.
class EmployeeAdmin(ModelAdmin):    
        list_display = ['empNo','empName','empMobile','empEmail']


admin.site.register(Employee,EmployeeAdmin)
