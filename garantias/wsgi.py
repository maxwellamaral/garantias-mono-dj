"""
WSGI config for garantias project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from manage import get_secret
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', get_secret("DJANGO_SETTINGS_MODULE"))

application = get_wsgi_application()
