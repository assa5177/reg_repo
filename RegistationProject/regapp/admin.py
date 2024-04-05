from django.contrib import admin
from regapp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    Employee_list=['EName','Enumber','EAddress','Esal']
admin.site.register(Employee,EmployeeAdmin)    