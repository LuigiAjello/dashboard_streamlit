
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Obter o diretório do arquivo atual e configurar o caminho
caminho = Path(__file__).resolve().parent / "data" / "ibov.csv"

# Título e cabeçalho do app
st.title("Meu primeiro dashboard")
st.header("Esse é um header")

# Exemplo de Markdown
st.markdown(
    '''
    # 1
    ## 2
    ### 3
    '''
)

# Criação de abas
abas = st.tabs(["Botão", "Radio", "DataFrame", "Gráfico"])

# Aba do botão
with abas[0]:
    if st.button("Clique aqui"):
        st.text("Você apertou o botão")

# Aba do radio (com a escolha do time)
with abas[1]:
    opcao = st.radio("Escolha seu time:", ["flamengo", "corinthians", "outro"])
    
    if opcao == "flamengo":
        st.info("Você é um urubu")
    elif opcao == "corinthians":
        st.warning("Você é um bobo")
    else:
        st.error("Você é um perdedor")

# Aba do DataFrame
with abas[2]:
    st.subheader("Exibição do DataFrame")
    
    # Verificar se o arquivo existe e, em caso afirmativo, exibir o DataFrame
    if caminho.exists():
        df = pd.read_csv(caminho)
        st.dataframe(df)
    else:
        st.error("Arquivo não encontrado: " + str(caminho))

# Aba do gráfico
with abas[3]:
    # Fixar o estado aleatório para reprodutibilidade
    np.random.seed(19680801)

    # Dados de exemplo
    fig, ax = plt.subplots()
    people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
    y_pos = np.arange(len(people))
    performance = 3 + 10 * np.random.rand(len(people))
    error = np.random.rand(len(people))

    # Criando o gráfico de barras horizontais
    ax.barh(y_pos, performance, xerr=error, align='center')
    ax.set_yticks(y_pos, labels=people)
    ax.invert_yaxis()  # Inverter ordem das labels
    ax.set_xlabel('Performance')
    ax.set_title('How fast do you want to go today?')

    # Exibir o gráfico no Streamlit
    st.pyplot(fig)