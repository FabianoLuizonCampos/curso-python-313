import streamlit as st

with st.sidebar:
    st.title("Calculadora IMC")

    st.header("IMC - Índice de Massa Corporal")

st.title("Calculadora")

peso = st.number_input(label="Digite o seu peso em kg", min_value=0.0)

altura = st.number_input(label="Digite o sua altura em metros", min_value=0.0)

if st.button("Calcular"):

    imc = peso / (altura ** 2)
    imc = round(imc, 2)

    st.write(f"Seu IMC é {imc}")