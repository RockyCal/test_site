from django.contrib import admin
from harddrives.models import Employee, Location, Box, Harddrive, File

class HarddriveAdmin(admin.ModelAdmin): 
    fieldsets = [
        ('Scan Serialnumber' , {'fields': ['serial_number']}),
        ('Date information', {'fields': ['startup_date']}),
        ('Owner',{'fields':['owner']}),
        ('File',{'fields':['file']}),
    ]

class LocationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Where it is', {'fields': ['name']}),
    ]

class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Employee Number', {'fields':['id_number']}),
        ('isabox', {'fields': ['isabox']}),
    ] 

class BoxAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Location', {'fields': ['location']}),
        ('Box Number', {'fields': ['name']}),
        ('isabox', {'fields': ['isabox']}),
    ]

class FileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
    ]


admin.site.register(File, FileAdmin)
admin.site.register(Box, BoxAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Harddrive, HarddriveAdmin)
