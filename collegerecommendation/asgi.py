# for asynchronous request handling by the django server

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'collegerecommendation.settings')

application = get_asgi_application()
