from models import *
from django.contrib import admin


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'secondary_email')
    search_fields = ('description', 'name',)
    list_per_page = 10
    save_on_top = True


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    list_filter = ['owner', 'start_date', 'stop_date']
    search_fields = ('description', 'name',)
    list_per_page = 10
    save_on_top = True

class NicInline(admin.TabularInline):
    model = Nic
    extra = 4

class InfrastructureAdmin(admin.ModelAdmin):
    list_display = ('data_center_code', 'hostname', 'role', 'type', 'operating_system')
    list_per_page = 20
    list_filter = ['role', 'type', 'rackno']
    search_fields = ('hostname', 'server_type',)
    save_on_top = True
    inlines = [NicInline]


class InfrastructureTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 20
    search_fields = ('name', 'description',)
    save_on_top = True


class InfrastructureRoleAdmin(admin.ModelAdmin):
    list_display = 'name'
    list_per_page = 20
    search_fields = ('name', 'description')
    save_on_top = True


class InstanceAdmin(admin.ModelAdmin):
    list_display = ('project', 'machine', 'name', 'ram', 'cpu', 'hdd')
    list_per_page = 20
    list_filter = ['project', 'machine', 'hypervisor', 'glance_image']
    search_fields = ('name', 'description',)
    save_on_top = True


class PortInline(admin.TabularInline):
    model = Port
    extra = 4


class RouterAdmin(admin.ModelAdmin):
    list_display = ('name', 'internal_ip', 'external_ip')
    list_per_page = 20
    list_filter = ['project', ]
    search_fields = ('internal_ip', 'name', 'external_ip')
    save_on_top = True
    inlines = [PortInline]


class NetworkInline(admin.TabularInline):
    model = Network
    extra = 1


class UserInline(admin.TabularInline):
    model = User
    extra = 3


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'stop_date', 'owner')
    list_per_page = 20
    list_filter = ['start_date', 'stop_date', 'owner', ]
    search_fields = ('description', 'name', 'resources')
    save_on_top = True
    inlines = [NetworkInline, UserInline]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Router, RouterAdmin)
admin.site.register(Infrastructure, InfrastructureAdmin)
admin.site.register(InfrastructureType, InfrastructureTypeAdmin)
admin.site.register(InfrastructureRole, InfrastructureRoleAdmin)
admin.site.register(Instance, InstanceAdmin)