web: gunicorn straymapper.wsgi -b 0.0.0.0:$PORT
celeryd: celery -A straymapper worker -E -B --loglevel=INFO
