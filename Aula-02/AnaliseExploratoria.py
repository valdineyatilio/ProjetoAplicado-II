#Bibliotecas python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar a base de dados do arquivo CSV
url = "https://github.com/valdineyatilio/ProjetoAplicado-II/raw/refs/heads/main/Aula-02/BaseDeDadosYouTube.csv"
dados_youtube = pd.read_csv(url, encoding='latin1')

# Vizualição das primeiras linhas do data frame
print(dados_youtube.head())

# Verificar informações sobre as colunas e tipos de dados
print(dados_youtube.info())

# Resumo estatístico das variáveis numéricas
print(dados_youtube.describe())
