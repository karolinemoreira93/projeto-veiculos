# Projeto de Análise de Anúncios de Veículos

## Descrição
Este projeto apresenta uma análise exploratória de anúncios de veículos usados. Foi desenvolvida uma aplicação web interativa para explorar os preços dos veículos e a relação entre preço e quilometragem.

## Aplicação online
Acede à aplicação através do link:

**https://projeto-veiculos-u2un.onrender.com/**

## Tecnologias utilizadas
- Python
- Pandas
- Plotly Express
- Streamlit

## Funcionalidades
- Visualização da distribuição dos preços dos veículos através de um histograma.
- Visualização da relação entre quilometragem e preço através de um gráfico de dispersão.

## Arquivos do projeto
- `app.py`: código da aplicação web.
- `vehicles_us.csv`: conjunto de dados utilizado.
- `vehicles_us_clean.csv`: conjunto de dados após o tratamento dos valores em falta.
- `requirements.txt`: bibliotecas necessárias para executar a aplicação.
- `notebooks/EDA.ipynb`: notebook de análise exploratória.
- `.streamlit/config.toml`: configurações do Streamlit.

## Como executar localmente
Instala as dependências com:

```bash
pip install -r requirements.txt
```

Depois, executa:

```bash
streamlit run app.py
```