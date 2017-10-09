web: gunicorn config.wsgi:application
worker: celery worker --app=octopus.taskapp --loglevel=info
