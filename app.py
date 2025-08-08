from flask import Flask, render_template, request, jsonify
import requests
import base64
import os
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    empresa = request.form['empresa'].strip().lower()
    codrodada = request.form['codrodada'].strip().lower()
    email_lider = request.form['email_lider'].strip().lower()
    
    # URL da API para buscar JSON do gráfico comparativo
    url_comparativo = f"https://hrkey-v2-grafico.onrender.com/buscar-json-supabase?tipo_relatorio=arquetipos_grafico_comparativo&empresa={empresa}&codrodada={codrodada}&emaillider={email_lider}"
    
    # URL da API para buscar JSON do relatório analítico
    url_analitico = f"https://hrkey-v2-grafico.onrender.com/buscar-json-supabase?tipo_relatorio=arquetipos_analitico&empresa={empresa}&codrodada={codrodada}&emaillider={email_lider}"
    
    try:
        response_comparativo = requests.get(url_comparativo)
        response_analitico = requests.get(url_analitico)
        
        if response_comparativo.status_code == 200:
            data_comparativo = response_comparativo.json()
            grafico_base64 = data_comparativo["grafico_base64"]
        else:
            grafico_base64 = None
            
        if response_analitico.status_code == 200:
            data_analitico = response_analitico.json()
            dados_analitico = data_analitico["dados"]
        else:
            dados_analitico = []
            
        return jsonify({
            'success': True,
            'grafico_base64': grafico_base64,
            'dados_analitico': dados_analitico
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
