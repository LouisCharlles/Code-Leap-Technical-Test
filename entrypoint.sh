#!/bin/bash
# entrypoint.sh

# Aplicar migrations
echo "Aplicando migrations..."
python manage.py migrate --noinput

# Coletar static files (caso use)
# python manage.py collectstatic --noinput

# Rodar Gunicorn
echo "Iniciando servidor Gunicorn..."
exec gunicorn setup.wsgi:application --bind 0.0.0.0:8000 --workers 3
