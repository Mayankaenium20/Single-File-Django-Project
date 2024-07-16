#SETTINGS.PY
from django.conf import settings
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
settings.configure(
    DEBUG=True,
    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32)),
    ROOT_URLCONF=__name__,
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ],
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'django.contrib.sessions',
        'django.contrib.messages',
    ],
)


#VIEWS.PY: handling http requests, queries, or the necessary data that needs to send for the presentation
from django.http import HttpResponse
# from django.conf.urls import url - depricated
from django.urls import path

def index(request):
    return HttpResponse(f"Hello World! {settings.SECRET_KEY}")             #the secret key can't be printed directly and hence "settings.SECRET_KEY" is used for proper syntax

def foo_fn(request):
    return HttpResponse(f"2+2 = {2+2}")

#URLS.PY: views associates with the url patters by pairing a regular expression to match the URL and any callable argument to the view.
urlpatterns = (
    path('', index),
    path('foo_fn/', foo_fn),
)

#WSGI.PY
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


#execution from terminal:
import sys
if __name__=='__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)