import os
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'wger.settings'  # Force set (override any default)
os.environ['PYTHONPATH'] = os.path.dirname(os.path.abspath(__file__))  # Add dir of wsgi.py
application = get_wsgi_application()
__init__.py
