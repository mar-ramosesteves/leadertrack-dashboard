import streamlit as st
import requests

st.set_page_config(page_title="LeaderTrack - Dashboard de Arquétipos", layout="wide")

st.title("📊 LeaderTrack - Dashboard de Arquétipos")

st.markdown("Preencha os dados abaixo para visualizar seus resultados:")

# Campos de entrada
empresa = st.text_input("Nome da empresa")
codrodada = st.text_input("Código da rodada")
email_lider = st.text_input("E-mail do líder")

if st.button("🔍 Buscar Resultados"):
    if not empresa or not codrodada or not email_lider:
        st.warning("Por favor, preencha todos os campos acima.")
    else:
        st.success("Buscando dados no Supabase...")

        # Formatação dos dados
        empresa = empresa.strip().lower()
        codrodada = codrodada.strip().lower()
        email_lider = email_lider.strip().lower()

        # URL da API para buscar JSON do gráfico comparativo
        url_comparativo = f"https://hrkey-v2-grafico.onrender.com/buscar-json-supabase?tipo_relatorio=arquetipos_grafico_comparativo&empresa={empresa}&codrodada={codrodada}&emaillider={email_lider}"

        # URL da API para buscar JSON do relatório analítico
        url_analitico = f"https://hrkey-v2-grafico.onrender.com/buscar-json-supabase?tipo_relatorio=arquetipos_analitico&empresa={empresa}&codrodada={codrodada}&emaillider={email_lider}"

        try:
            response_comparativo = requests.get(url_comparativo)
            response_analitico = requests.get(url_analitico)

            if response_comparativo.status_code == 200:
                data = response_comparativo.json()
                st.markdown("### 🎯 Gráfico Comparativo: Autoavaliação vs Equipe")
                st.image(data["grafico_base64"])
            else:
                st.error("❌ Erro ao buscar o gráfico comparativo.")

            if response_analitico.status_code == 200:
                data = response_analitico.json()
                st.markdown("### 📋 Relatório Analítico por Afirmação")
                for grupo in data["dados"]:
                    st.markdown(f"#### 🔹 {grupo['grupoArquetipo']}")
                    for item in grupo["questoes"]:
                        questao = item["questao"]
                        auto = item["autoavaliacao"]
                        equipe = item["mediaEquipe"]

                        col1, col2, col3 = st.columns([3, 1, 1])
                        col1.markdown(f"- {questao}")
                        col2.progress(auto / 100)
                        col3.progress(equipe / 100)
            else:
                st.error("❌ Erro ao buscar o relatório analítico.")

        except Exception as e:
            st.error(f"Erro ao buscar dados: {e}")
