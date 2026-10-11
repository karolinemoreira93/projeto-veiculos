
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.header("Análise de anúncios de veículos")

# Carregar os dados
car_data = pd.read_csv("vehicles_us.csv")

st.write("Explore os dados dos anúncios de veículos usados.")

# Botão para criar um histograma
if st.button("Mostrar histograma dos preços"):
    fig = px.histogram(
        car_data,
        x="price",
        title="Distribuição dos preços dos veículos",
        labels={"price": "Preço (€)"}
    )
    st.plotly_chart(fig, use_container_width=True)

# Botão para criar um gráfico de dispersão
if st.button("Mostrar gráfico de dispersão"):
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Preço dos veículos em função da quilometragem",
        labels={
            "odometer": "Quilometragem",
            "price": "Preço (€)"
        }
    )
    st.plotly_chart(fig, use_container_width=True)
