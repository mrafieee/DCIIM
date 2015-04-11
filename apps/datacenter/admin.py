from models import *
from django.contrib import admin


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'secondary_email')
    search_fields = ('description', 'name',)
    list_per_page = 10
    save_on_top = True

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    list_filter = ['customer']
    search_fields = ('description', 'name',)
    list_per_page = 10
    save_on_top = True

# class SampleInline(admin.TabularInline):
#     model = Media
#     extra = 2
#     exclude = ('type',)


class InfraAdmin(admin.ModelAdmin):
    list_display = ('data_center_code', 'hostname', 'role', 'server_type', 'operating_system')
    list_per_page = 20
    list_filter = ['role', 'server_type']
    search_fields = ('hostname', 'server_type',)
    save_on_top = True
    #inlines = [MediaInline]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Infrastructure, InfraAdmin)
