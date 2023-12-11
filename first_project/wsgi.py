"""
WSGI config for first_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

application = get_wsgi_application()

# for i in range(1,13):
    #  print(i)

# second day - for testing 
# a = [1, 2, 3, 4]
# print(a)    