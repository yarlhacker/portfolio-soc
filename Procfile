release: python manage.py migrate && python init_db.py
web: gunicorn portfolio.wsgi --log-file -