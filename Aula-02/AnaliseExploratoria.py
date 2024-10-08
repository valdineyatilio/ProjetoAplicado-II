#Bibliotecas python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Carregar a base de dados do arquivo CSV
url = "https://github.com/valdineyatilio/ProjetoAplicado-II/raw/refs/heads/main/Aula-02/BaseDeDadosYouTube.csv"
dados_youtube = pd.read_csv(url, encoding='latin1')

# Vizualição das primeiras linhas do data frame
print(dados_youtube.head())

# Verificar os nomes das colunas
print(dados_youtube.columns)

# Verificação de Tipos de Dados
for coluna in dados_youtube.columns:
    if dados_youtube[coluna].dtype == 'object':
        dados_youtube[coluna] = dados_youtube[coluna].astype('category')
    elif dados_youtube[coluna].dtype in ['int64', 'float64']:
        dados_youtube[coluna] = dados_youtube[coluna].astype(float)

# Verificação das informações das colunas
print(dados_youtube.info())

# Resumo estatístico das variáveis numéricas
print(dados_youtube.describe())

# Visualizações gráficas 
plt.figure(figsize=(14, 6))
dados_youtube.hist(bins=30, figsize=(20,15))
plt.suptitle('Histogramas das Variáveis Numéricas')
plt.show()

# Histograma das visualizações
plt.figure(figsize=(10, 6))
plt.hist(dados_youtube['video views'], bins=30, color='skyblue', edgecolor='black')
plt.title('Histograma de Visualizações')
plt.xlabel('Visualizações')
plt.ylabel('Contagem')
plt.grid(True)
plt.show()

# Gráfico de dispersão de visualização vs. país
plt.figure(figsize=(10, 6))
plt.scatter(dados_youtube['video views'], dados_youtube['country_rank'], alpha=0.5, color='green')
plt.title('Visualização vs País')
plt.xlabel('Visualização')
plt.ylabel('País')
plt.grid(True)
plt.show()

# Gráfico de barras do número de vídeos por categoria
plt.figure(figsize=(10, 6))
dados_youtube['category'].value_counts().plot(kind='bar', color='orange', fontsize=8)
plt.title('Número de Vídeos por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Rank')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Identificação de valores ausentes
print("\nValores Ausentes:")
print(dados_youtube.isnull().sum())

# Identificação de outliers usando Z-score
from scipy import stats
z_scores = np.abs(stats.zscore(dados_youtube.select_dtypes(include=[np.number])))
outliers = (z_scores > 3).sum(axis=1)
print("\nNúmero de outliers em cada linha:")
print(outliers)

# Boxplot para identificar outliers
plt.figure(figsize=(12, 6))
sns.boxplot(data=dados_youtube.select_dtypes(include=[float]), orient='h')
plt.title('Boxplot das Variáveis Numéricas')
plt.show()

# Removendo outliers
df_clean = dados_youtube[(z_scores < 3).all(axis=1)]
print("\nDataFrame após remoção de outliers:")
print(df_clean.describe())

# Análise de Correlação
# Selecionando colunas numericas  e calculando a correlação
numeric_data = dados_youtube.select_dtypes(include=[float, int])
correlacao = numeric_data.corr()

# Mapa de calor da correlação
plt.figure(figsize=(10, 8))
sns.heatmap(correlacao, annot=True, cmap='coolwarm', center=0)
plt.title('Mapa de Calor da Correlação')
plt.show()