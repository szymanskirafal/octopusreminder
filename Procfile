web: gunicorn config.wsgi:application
worker: celery worker -B --app=octopus.taskapp --loglevel=info
