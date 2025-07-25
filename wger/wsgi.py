"""
WSGI config for workout_manager project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""

# Standard Library
import os

# Django
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wger.settings')

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
application = get_wsgi_application()

import os
import sys
print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
print("SETTINGS_MODULE:", os.environ.get('DJANGO_SETTINGS_MODULE'))
print("SYS.PATH:", sys.path)
try:
    import wger.settings
    print("Import successful")
except ImportError as e:
    print("Import failed:", e)

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
