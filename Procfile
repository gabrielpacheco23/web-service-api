web: gunicorn --worker-class eventlet -w 1 manage:app
init: python3 manage.py db init
migrate: python3 manage.py db migrate --directory app/migrations
upgrade: python3 manage.py db upgrade --directory app/migrations
