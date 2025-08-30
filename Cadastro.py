import streamlit as st
import pandas as pd
import datetime 
from datetime import date


def gravar_dados(nome, dt_nasc, tipo_cliente):
    if nome and dt_nasc <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome}, {dt_nasc}, {tipo_cliente}\n")
        st.session_state["Sucesso"] = True
    else:
        st.session_state["Sucesso"] = False


st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="👧🏽" 
)

st.title("Cadastro de Clientes")

st.divider()

nome = st.text_input("Digite o nome do cliente",
                     key="nome_cliente")

# Define a data mínima e máxima

min_date = datetime.date(1900, 1, 1)
max_date = datetime.date(2100, 12, 31)

# Use st.date_input com os parâmetros min_value e max_value

dt_nasc = st.date_input("Data de nascimento",
                     value=datetime.date(2024, 1, 1),
                     min_value=min_date, max_value=max_date)


tipo_cliente = st.selectbox("Tipo do Cliente",
                            ["Pessoa jurídica", "Pessoa Física"])

btn_cadastro = st.button("Cadastrar",
                         on_click=gravar_dados,
                         args=[nome, dt_nasc, tipo_cliente])

if btn_cadastro:
    if st.session_state["Sucesso"]:
        st.success("Cliente cadastrado com sucesso!",
                   icon="✨")
    else:
        st.error("Houve algum problema no cadastro!",
                 icon="🧨")