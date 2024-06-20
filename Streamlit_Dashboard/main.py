# pip install streamlit
# streamlit run main.py
# pip install pandas

import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("Analise de Lucro")

    uploaded_file = st.file_uploader("Coloque seu arquivo aqui")

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    with st.sidebar:

        regioes = df["Region"].unique().tolist()

        selecao_regiao = st.selectbox("Região Específica", regioes)

        selecao_prioridade = st.radio("Prioridade",["H", "C", "M", "L"], index=None)

        if selecao_regiao:
            df = df[df["Region"] == selecao_regiao]

        if selecao_prioridade:
            df = df[df["Order Priority"] == selecao_prioridade]

    st.write("Lucro por tipo de item")

    st.bar_chart(df, x="Item Type", y="Total Profit")

    st.dataframe(df, use_container_width=True)