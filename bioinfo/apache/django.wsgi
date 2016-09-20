import os, sys
sys.path.append('/wwwdata/apps')
sys.path.append('/wwwdata/apps/bioinfo')
os.environ['DJANGO_SETTINGS_MODULE'] = 'bioinfo.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
