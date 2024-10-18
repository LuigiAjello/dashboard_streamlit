import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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
    st.subheader("Gráfico do Fechamento do Ibovespa ao longo do tempo")

    if caminho.exists():
        df = pd.read_csv(caminho)

        # Verificar se as colunas necessárias existem
        if 'data' in df.columns and 'fechamento' in df.columns:
            # Converter a coluna 'data' para o tipo datetime
            df['data'] = pd.to_datetime(df['data'])

            # Criar o gráfico de linha para o valor de fechamento do Ibovespa ao longo do tempo
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(df['data'], df['fechamento'], label='Fechamento Ibovespa', color='b')

            # Configurar o título e os rótulos do gráfico
            ax.set_title('Fechamento do Ibovespa ao longo do tempo', fontsize=14)
            ax.set_xlabel('Data', fontsize=12)
            ax.set_ylabel('Fechamento (R$)', fontsize=12)

            # Adicionar uma grade
            ax.grid(True)

            # Mostrar a legenda
            ax.legend()

            # Ajustar os ticks e layout
            plt.xticks(rotation=45)
            plt.tight_layout()

            # Exibir o gráfico no Streamlit
            st.pyplot(fig)
        else:
            st.error("O arquivo não contém as colunas necessárias ('data' e 'fechamento').")
    else:
        st.error("Arquivo não encontrado: " + str(caminho))
