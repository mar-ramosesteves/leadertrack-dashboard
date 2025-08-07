#!/bin/bash
echo "Verificando se streamlit está instalado..."
python -c "import streamlit; print('Streamlit encontrado!')"
echo "Iniciando aplicação..."
python -m streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
