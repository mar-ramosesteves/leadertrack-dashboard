#!/bin/bash
echo "=== ESTE É UM PROJETO FLASK ==="
echo "Limpando qualquer cache do streamlit..."
pip uninstall streamlit -y 2>/dev/null || true
echo "Instalando dependências Flask..."
pip install -r requirements.txt
echo "=== BUILD CONCLUÍDO COM FLASK ==="