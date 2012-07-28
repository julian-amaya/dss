web: gunicorn dss.wsgi -b 0.0.0.0:$PORT
celeryd: python manage.py celeryd -E  --loglevel=INFO