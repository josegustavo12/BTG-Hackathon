#!/bin/bash

# Script para parar processos na porta 8000 e iniciar o Docker

echo "Verificando processos na porta 8000..."
PID=$(lsof -ti:8000)

if [ ! -z "$PID" ]; then
    echo "Encontrado processo $PID usando a porta 8000"
    echo "Parando processo..."
    kill -9 $PID
    echo "Processo parado!"
    sleep 1
fi

echo "Iniciando containers Docker..."
sudo docker-compose up --build
