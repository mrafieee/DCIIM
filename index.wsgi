#!/bin/python
import os
import sys
sys.path.append('/var/www/DCIIM/')
sys.path.append('/usr/lib/python2.7/dist-packages/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'dciim.settings'
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
