release: python manage.py migrate && python manage.py collectstatic --noinput && python init_db.py
web: gunicorn portfolio.wsgi --log-file - --access-logfile - --error-logfile -