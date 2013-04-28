import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'run4me.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
