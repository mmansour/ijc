# pinax.wsgi is configured to live in projects/mrcancel/deploy.

import os
import sys

# redirect sys.stdout to sys.stderr for bad libraries like geopy that uses
# print statements for optional import exceptions.
sys.stdout = sys.stderr

from site import addsitedir
addsitedir('/home/mattym/envs/mezz118/lib/python2.6/site-packages')

from os.path import abspath, dirname, join
from django.conf import settings

os.environ["DJANGO_SETTINGS_MODULE"] = "ijcdigital.settings"
sys.path.insert(0, join(settings.PROJECT_ROOT, "apps"))
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
