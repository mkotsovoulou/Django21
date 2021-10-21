release: python manage.py migrate
web: gunicorn --chdir djone djone.wsgi:application --log-file - --log-level debug
