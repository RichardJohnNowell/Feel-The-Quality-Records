"""
WSGI config for feelthequalityrecords project.
"""


import os


from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feelthequalityrecords.settings')


application = get_wsgi_application()


#end
