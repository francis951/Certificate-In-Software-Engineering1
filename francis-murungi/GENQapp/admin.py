from django.contrib import admin
from .models import GENQModels
# Register your models here.

class GENQModelsAdmin(admin.ModelAdmin):
    list_display = ['f_name','l_name', 'date', 'gender', 'country', 'state','town', 'zip','phone1','phone2', 'email']
    search_fields = ['f_name', 'phone1', 'email']
    list_per_page = 10
    
admin.site.register(GENQModels, GENQModelsAdmin)