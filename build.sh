#!/bin/bash
echo "Instalando dependências..."
pip install --upgrade pip
pip install streamlit==1.28.1 plotly==5.17.0 requests==2.31.0
echo "Verificando instalação do streamlit..."
python -c "import streamlit; print('Streamlit instalado com sucesso!')"
echo "Build concluído!"
