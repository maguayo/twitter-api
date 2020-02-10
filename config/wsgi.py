import os
import sys
import environ
from django.core.wsgi import get_wsgi_application
from os.path import dirname as up
from dotenv import load_dotenv
from os.path import join

# This allows easy placement of apps within the interior
# project directory.
app_path = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
)
sys.path.append(os.path.join(app_path, "project"))

BASE_PATH = up(up(__file__))
dotenv_path = join(BASE_PATH, '.env')
load_dotenv(dotenv_path)

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.production"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
application = get_wsgi_application()