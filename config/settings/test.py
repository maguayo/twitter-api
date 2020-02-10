from .base import *  # NOQA
from .base import env

# Base
DEBUG = False

# NEVER write the key here, this is just an example
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="7lEaACt4wsCj8JbXYgQLf4BmdG5QbuHTMYUGir2Gc1GHqqb2Pv8w9iXwwlIIviI2",
)