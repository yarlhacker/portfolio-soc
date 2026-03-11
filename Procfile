release: python manage.py migrate && python init_db.py && python reset_admin.py
web: gunicorn portfolio.wsgi --log-file -