release: sh -c 'python manage.py migrate && python manage.py loaddata initial_katalog_data.json'
web: gunicorn project_django.wsgi --log-file -