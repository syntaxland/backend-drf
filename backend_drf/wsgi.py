"""
WSGI config for backend_drf project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

# import os


# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_drf.settings')

# application = get_wsgi_application()


import os

# import pathlib  # Added
# import dotenv  # Added

from django.core.wsgi import get_wsgi_application

# CURRENT_DIR = pathlib.Path(__file__).resolve().parent  # Added
# BASE_DIR = CURRENT_DIR.parent  # Added
# ENV_FILE_PATH = BASE_DIR / ".env"  # Added
# dotenv.read_dotenv(str(ENV_FILE_PATH))  # Added

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_drf.settings')
application = get_wsgi_application()
