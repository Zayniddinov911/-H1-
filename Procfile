release: python manage.py makemigrations --no-input && python manage.py migrate --no-input

web: gunicorn mars.wsgi