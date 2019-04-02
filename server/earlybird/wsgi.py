"""
WSGI config for earlybird project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""
#!/usr/bin/python
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "earlybird.settings")

application = get_wsgi_application()


import subprocess 
p = os.getcwd()
a = "/web/groups/earlybirdsystem/public_html/process_tasks.sh"
#subprocess.call(a)
