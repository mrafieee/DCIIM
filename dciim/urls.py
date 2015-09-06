from django.conf.urls import include, url
from django.contrib import admin
from dciim import settings

urlpatterns = [
    url(r'^$', 'apps.views.home', name='home'),
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.BASE_DIR + '/static/'}),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.BASE_DIR + '/media/'}),
    url(r'^static/admin/(.*)$', 'django.views.static.serve', {'document_root': settings.BASE_DIR + '/static/admin/'}),

    url(r'^generate-report/$','apps.datacenter.views.list_backup_files', name='list'),
    url(r'^extract-zip-file/(?P<file>[\w\.-]+)/$','apps.datacenter.views.extract', name='extract'),

    url(r'^reports/$','apps.datacenter.views.reports', name='reports'),
    url(r'^reports/projects-list/$','apps.datacenter.views.list_projects', name='list-projects'),
    url(r'^reports/routers-list/$','apps.datacenter.views.list_routers', name='list-routers'),
    url(r'^reports/subnets-list/$','apps.datacenter.views.list_subnets', name='list-subnets'),
    url(r'^reports/floating-ip-list/$','apps.datacenter.views.list_floating_ip', name='list-floating-ips'),
    url(r'^reports/demo-vpc-list/$','apps.datacenter.views.list_demo_vpc', name='list-demo-vpc'),
    url(r'^reports/instances-list/$','apps.datacenter.views.list_instances', name='list-instances'),

    url(r'^history$','apps.datacenter.views.history', name='history'),

    url(r'^admin/', include(admin.site.urls)),
]
