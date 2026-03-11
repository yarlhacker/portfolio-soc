release: python manage.py migrate && python init_db.py && python reset_admin.py
web: gunicorn --bind 0.0.0.0:$PORT portfolio.wsgi:application