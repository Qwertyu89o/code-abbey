"""
ASGI config for CodeAbbey project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django.core.asgi

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CodeAbbey.settings')
application = django.core.asgi.get_asgi_application()
