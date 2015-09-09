"""
WSGI config for dciim project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dciim.settings")

path = '/var/www/dciim/'

if path not in sys.path:
	sys.path.append(path)

print sys.path

application = get_wsgi_application()
