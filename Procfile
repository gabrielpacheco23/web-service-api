web: gunicorn --worker-class eventlet -w 1 manage:app
init: python3 manage.py db init
migrate: python3 manage.py db migrate 
upgrade: python3 manage.py db upgrade
