"""CodeAbbey URL Configuration

The `urlpatterns` list routes URLs to views.

For more information please see:
https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""

import django.urls

urlpatterns = [
    django.urls.path('', django.urls.include('app.urls')),
]
