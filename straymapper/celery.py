import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "straymapper.settings")

app = Celery('straymapper')

# Read CELERY_* settings from the Django settings module.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load tasks.py from all installed apps.
app.autodiscover_tasks()
