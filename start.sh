#!/bin/bash
echo "Verificando se Flask está instalado..."
python -c "import flask; print('Flask encontrado!')"
echo "Iniciando aplicação Flask..."
python app.py
