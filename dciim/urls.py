from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'dciim.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^list/$','apps.datacenter.views.list_backup_files', name='list'),
    url(r'^extract-zip-file/(?P<file>[\w\.-]+)/$','apps.datacenter.views.extract', name='extract'),
    url(r'^import/$','apps.datacenter.views.import_databases', name='import'),

    url(r'^list/projects/$','apps.datacenter.views.list_projects', name='list-projects'),

    url(r'^', include(admin.site.urls)),
]
