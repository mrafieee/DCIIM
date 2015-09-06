from models import *
from django.contrib import admin

class NicInline(admin.TabularInline):
    model = Nic
    extra = 1

class ChangesInline(admin.TabularInline):
    model = Changes
    extra = 1

class InfrastructureAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'data_center_code', 'role','group', 'type', 'operating_system')
    list_per_page = 70
    list_filter = ['role', 'type', 'rack_number','group']
    search_fields = ('hostname', 'server_type',)
    save_on_top = True
    inlines = [NicInline,ChangesInline]

class InfrastructureRoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 20
    search_fields = ('name', 'description',)
    save_on_top = True

class InfrastructureTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 20
    search_fields = ('name', 'description',)
    save_on_top = True

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('backup_file',
                    'instance_count',
                    'projects_count',
                    'routers_count',
                    'floating_ips_count',
                    'network_count',
                    'images_count',
                    'compute_node_count',
                    'total_vcpu',
                    'total_memory',
                    'total_local_disk')
    list_per_page = 70
    save_on_top = True

admin.site.register(History, HistoryAdmin)
admin.site.register(Infrastructure, InfrastructureAdmin)
admin.site.register(InfrastructureRole, InfrastructureRoleAdmin)
admin.site.register(InfrastructureType, InfrastructureTypeAdmin)
