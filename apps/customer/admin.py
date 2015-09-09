from models import *
from django.contrib import admin

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_point_full_name', 'cell_phone', 'email', 'service_type')
    list_per_page = 50
    list_filter = ['service_type',]
    search_fields = ('company_name', 'description', 'contact_point_full_name','email')
    save_on_top = True

admin.site.register(Customer, CustomerAdmin)
