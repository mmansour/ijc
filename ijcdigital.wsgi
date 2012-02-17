
import os, sys

# activate virtualenv
activate_this = os.path.expanduser("/home/mattym/envs/mezz118/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

# tell django where our settings module is
sys.path.insert(0, os.path.expanduser("/home/mattym/webapps/mezzanine_server"))
sys.path.insert(1, os.path.expanduser("/home/mattym/webapps/mezzanine_server/ijcdigital"))
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# run django
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()





# OLD pinax.wsgi is configured to live in projects/mrcancel/deploy.

#import os
#import sys

# redirect sys.stdout to sys.stderr for bad libraries like geopy that uses
# print statements for optional import exceptions.
#sys.stdout = sys.stderr

#from site import addsitedir
#addsitedir('/home/mattym/envs/mezz118/lib/python2.6/site-packages')
#addsitedir('/home/mattym/webapps/mezzanine_server/ijcdigital')

#from os.path import abspath, dirname, join
#from django.conf import settings

#os.environ["DJANGO_SETTINGS_MODULE"] = "ijcdigital.settings"
#sys.path.insert(0, join(settings.PROJECT_ROOT, "apps"))
#sys.path.insert(1,'/home/mattym/webapps/mezzanine_server/ijcdigital')

#from django.core.handlers.wsgi import WSGIHandler
#application = WSGIHandler()
