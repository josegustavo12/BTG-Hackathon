#!/bin/bash

# Script para executar migrations no container Docker

echo "Executando migrations no container web..."
docker-compose exec web python manage.py migrate

echo "Migrations concluídas!"
